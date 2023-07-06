#
# Copyright (c) 2023 Commonwealth Scientific and Industrial Research Organisation (CSIRO). All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file. See the AUTHORS file for names of contributors.
#
from __future__ import annotations
from dataclasses import dataclass, field
from dataclass_wizard import JSONWizard, json_field
from argparse import ArgumentParser, Action, ArgumentTypeError
from typing import List, Any
import yaml
from enum import Enum
import validators
import os

from typing import Dict

from .utils import read_yaml_no_dates
from .ivcap import get_config, is_valid_resource_urn
from .config import Resource, INSIDE_CONTAINER

@dataclass
class Option:
    value: str
    name: str = None
    description: str = None

class Type(Enum):
    STRING = 'string'
    INT = 'int'
    FLOAT = 'float'
    BOOL = 'bool'
    OPTION = 'option'
    ARTIFACT = 'artifact'
    COLLECTION = 'collection'

@dataclass()
class Parameter(JSONWizard):
    class _(JSONWizard.Meta):
        skip_defaults = True

    name: str
    type: Type
    options: List[Option] = None
    description: str = None
    default: Any = None
    unit: str = None
    help: str = None
    optional: bool = False
    constant: bool = False

    def __post_init__(self):
        # 'default' is supposed to be a string
        self.default = self._to_str(self.default)

    def to_dict(self):
        d = super().to_dict()
        if self.type == Type.BOOL and not self.default:
            d['optional'] = True
        return d

    def _to_str(self, v):
        if v != None and type(v) != str:
            return str(v)
        else:
            return v

@dataclass
class Workflow(JSONWizard):
    class _(JSONWizard.Meta):
        skip_defaults = False

    type: str

@dataclass
class BasicWorkflow(Workflow):
    type: str = "basic"
    image: str = os.getenv('IVCAP_CONTAINER', '@CONTAINER@')
    command: List[str] = field(default_factory=list)
    min_memory: str = None

    def to_dict(self):
        basic = {
            'command': self.command,
            'image': self.image
        }
        if self.min_memory:
            basic['memory'] = { 'request': self.min_memory}
        return {
            'type': 'basic',
            'basic': basic
        }


@dataclass
class PythonWorkflow(BasicWorkflow):
    script: str = '/app/service.py'

    @classmethod
    def def_workflow(cls): 
        return cls()

    def to_dict(self):
        d = super().to_dict()
        d['basic']['command'] = ['python', self.script]
        return d

@dataclass
class Service(JSONWizard):
    # class _(JSONWizard.Meta):
    #     skip_defaults = True

    name: str
    id: str = os.getenv('IVCAP_SERVICE_ID', '@SERVICE_ID@')
    providerID: str = json_field('provider-id', all=True, default=os.getenv('IVCAP_PROVIDER_ID', '@PROVIDER_ID@'))
    accountID: str = json_field('account-id', all=True, default=os.getenv('IVCAP_ACCOUNT_ID', '@ACCOUNT_ID@'))
    parameters: List[Parameter] = field(default_factory=list)
    description: str = None
    workflow: Workflow = field(default_factory=PythonWorkflow.def_workflow)

    @classmethod
    def from_file(cls, serviceFile: str) -> None:
        pd = read_yaml_no_dates(serviceFile)
        return cls.from_dict(pd)

    # this function is NOT calling the 'to_dict' of referenced JSONWizard classes
    def to_dict(self):
        d = super().to_dict()
        d['parameters'] = list(map(lambda p: p.to_dict(), self.parameters))
        d['workflow'] = self.workflow.to_dict()
        return d

    def to_yaml(self) -> str:
        return yaml.dump(self.to_dict(), default_flow_style=False)

    def append_arguments(self, ap: ArgumentParser) -> ArgumentParser:
        type2type = {
            Type.STRING: str,
            Type.INT: int,
            Type.FLOAT: float,
            Type.BOOL: bool,
        }
        # optionals = []
        for p in self.parameters:
            if not (p.name and p.type):
                raise Exception(f"A service parameter needs at least a name and a type - {p}")
            name = p.name
            if name.startswith('cre:') or name.startswith('ivcap:'):
                continue
            args:Dict[str, Any] = dict(required = True)
            if p.type == Type.OPTION:
                ca = list(map(lambda o: o.value, p.options))
                args['choices'] = ca      
            elif p.type == Type.ARTIFACT:
                args['type'] = verify_artifact
                args['metavar'] = "URN"
                args['action'] = ArtifactAction
                pass
            elif p.type == Type.COLLECTION:
                args['type'] = verify_collection
                args['metavar'] = "URN"
                args['action'] = CollectionAction
                pass
            elif p.type == Type.BOOL:
                args['action'] ='store_true'
                args['required'] = False
            else:
                if not type(p.type) == Type:
                    raise Exception(f"Wrong type declaration for '{name}' - use enum 'Type'")
                   
                t = type2type.get(p.type)
                if not t:
                    raise Exception(f"Unsupported type '{p.type}' for '{name}'")
                args['type'] = t
                args['metavar'] = p.type.name.upper()
            if p.default:
                args['default'] = p.default
            if p.description:
                if p.default:
                    args['help'] = f"{p.description} [{p.default}]"
                else:
                    args['help'] = f"{p.description}"
            if p.optional:
                args['required'] = not p.optional
                # optionals.append(name)
            if p.constant or p.default:
                args['required'] = False
            ap.add_argument(f"--{name}", **args)
        return ap

# TODO: Add verifying code
def verify_artifact(urn):
    if is_valid_resource_urn(urn, Resource.ARTIFACT):
        return urn

    if INSIDE_CONTAINER:
        if not validators.url(urn):
            raise ArgumentTypeError(f"Illegal artifact reference '{urn}' - expected url")
        return urn
    else:
        if validators.url(urn):
            return urn
        # outside container we allow resource to be local file
        if not get_config().IO_ADAPTER.artifact_readable(urn):
            raise ArgumentTypeError(f"Cannot find local file '{urn}' - {get_config().IO_ADAPTER}")
        return urn

class ArtifactAction(Action):
    def __call__(self, _1, namespace, value, _2=None):
        try:
            v = get_config().IO_ADAPTER.read_artifact(value)
            setattr(namespace, self.dest, v)
        except Exception as err:
            raise ArgumentTypeError(err)

def verify_collection(urn):
    if is_valid_resource_urn(urn, Resource.COLLECTION):
        return urn
    if is_valid_resource_urn(urn, Resource.ARTIFACT):
        # treating a artifact as a collection of ONE
        return urn


    if INSIDE_CONTAINER:
        raise ArgumentTypeError(f"Illegal collection reference '{urn}' - expected url")
    else:
        # throws an exception if we can't create a collection object
        get_config().IO_ADAPTER.get_collection(urn)
        return urn 

class CollectionAction(Action):
    def __call__(self, _1, namespace, value, _2=None):
        try:
            v = get_config().IO_ADAPTER.get_collection(value)
            setattr(namespace, self.dest, v)
        except Exception as err:
            raise ArgumentTypeError(err)
