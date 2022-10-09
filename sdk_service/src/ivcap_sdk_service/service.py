from __future__ import annotations
from dataclasses import dataclass, field
from dataclass_wizard import JSONWizard, json_field
from argparse import ArgumentParser, Action, ArgumentTypeError
from typing import List, Any
import yaml
from enum import Enum

# import time
# from urllib.request import urlopen
# import re
# import argparse
# import os
# import sys
from typing import Dict
# from tempfile import NamedTemporaryFile

from .utils import read_yaml_no_dates
from .ivcap import get_config, is_valid_resource_urn
from .config import Resource, INSIDE_CONTAINER, verify_file

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

@dataclass
class Parameter:
    name: str
    type: Type
    options: List[Option] = None
    description: str = None
    default: str = None
    unit: str = None
    help: str = None
    optional: bool = False
    constant: bool = False

@dataclass
class Service(JSONWizard):
    class _(JSONWizard.Meta):
        skip_defaults = True

    name: str
    providerID: str = json_field('provider-id', all=True)
    parameters: List[Parameter] = field(default_factory=list)
    description: str = None
    id: str = None

    @classmethod
    def from_file(cls, serviceFile: str) -> None:
        pd = read_yaml_no_dates(serviceFile)
        return cls.from_dict(pd)

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
            #print(f">>>ADD: {name} - {args}")
            ap.add_argument(f"--{name}", **args)
        return ap

# TODO: Add verifying code
def verify_artifact(urn):
    if is_valid_resource_urn(urn, Resource.ARTIFACT):
        return urn
    if not INSIDE_CONTAINER:
        # outside container we allow resource to be local file
        if not get_config().IO_ADAPTER.readable(urn):
            raise ArgumentTypeError(f"XCannot find local file '{urn}' - {get_config().IO_ADAPTER}")
        return urn
    else:
        raise ArgumentTypeError(f"Illegal artifact urn '{urn}'")

class ArtifactAction(Action):
    def __call__(self, _1, namespace, value, _2=None):
        try:
            v = get_config().IO_ADAPTER.read(value)
            setattr(namespace, self.dest, v)
        except Exception as err:
            raise ArgumentTypeError(err)
        
        
# def get_command_line_args(pd, remaining, print_help):
#     """Read command line arguments with paramters built from 'product' file"""
    
#     global SERVICE_NAME
#     SERVICE_NAME = pd.get('id', 'unknown')
#     args = dict(prog = SERVICE_NAME, add_help=False);
#     d = pd.get('name'); 
#     if d: args['description'] = d
#     ap = argparse.ArgumentParser(**args)

#     optionals = []
#     for p in pd.get('parameters', []):
#         name = p['name']
#         if name.startswith('cre:'):
#           continue
#         args = dict(required = True)
#         if 'type' in p:
#             t = dict(int = int, float = float, string = str, option = str, number = float).get(p['type'])
#             if t: 
#               args['type'] = t
#         if 'default' in p:
#             args['default'] = p['default']
#         if 'description' in p:
#             if 'default' in p:
#               args['help'] = f"{p['description']} [{p['default']}]"
#             else:
#               args['help'] = f"{p['description']}"
#         if 'optional' in p:
#             args['required'] = not p['optional']
#             optionals.append(name)
#         if 'constant' in p and 'default' in p:
#             args['required'] = False
#         ap.add_argument(f"--{name}", **args)
#     if print_help:
#         add_arguments(ap)
#         ap.print_help()
#         return None
#     else:
#         args = vars(ap.parse_args(remaining)) # ['--north', '11']))
#         return {k:v for k,v in args.items() if v} # remove all None valued elements



# def main(service_file, out_data_dir, remaining, add_report, print_help):
#     pd = read_yaml_no_dates(service_file)
#     params = get_command_line_args(pd, remaining, print_help)
#     if params == None: return
#     verify_dir(out_data_dir)

#     if has_error:
#         sys.exit("error: Check logging messages for cause of error exit")
#     else:
#         os._exit(0)
