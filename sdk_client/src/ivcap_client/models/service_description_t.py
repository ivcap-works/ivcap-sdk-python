from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.parameter_def_t import ParameterDefT
from ..models.parameter_t import ParameterT
from ..models.reference_t import ReferenceT
from ..models.workflow_t import WorkflowT
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceDescriptionT")


@attr.s(auto_attribs=True)
class ServiceDescriptionT:
    """
    Example:
        {'account-id': 'cayp:account:acme', 'banner': 'http://stark.info/tess.gaylord', 'description': 'This service
            ...', 'metadata': [{'name': 'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'},
            {'name': 'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name': 'Odit aut
            quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name': 'Odit aut quod nihil aperiam.',
            'value': 'Ut enim ut fugit possimus pariatur.'}], 'name': 'Fire risk for Lot2', 'parameters': [{'description':
            'The name of the region as according to ...', 'label': 'Region Name', 'name': 'region', 'type': 'string'},
            {'label': 'Rainfall/month threshold', 'name': 'threshold', 'type': 'float', 'unit': 'm'}], 'provider-id':
            'cayp:provider:acme', 'provider-ref': 'service_foo_patch_1', 'references': [{'title': 'Commodi aut voluptatem
            magni.', 'uri': 'http://mclaughlintremblay.name/adam'}, {'title': 'Commodi aut voluptatem magni.', 'uri':
            'http://mclaughlintremblay.name/adam'}, {'title': 'Commodi aut voluptatem magni.', 'uri':
            'http://mclaughlintremblay.name/adam'}], 'tags': ['tag1', 'tag2'], 'workflow': {'argo': 'Sed ut in distinctio
            consequatur aut voluptas.', 'basic': {'command': ['Unde fuga sed veniam.', 'Et aut autem deserunt sit
            architecto.', 'Quidem nulla quae provident dolor amet nulla.'], 'cpu': {'limit': 'Deserunt fugiat hic eos
            quaerat voluptas distinctio.', 'request': 'Reprehenderit molestiae cupiditate voluptas et voluptatibus illum.'},
            'image': 'Officiis consequatur corporis autem.', 'memory': {'limit': 'Deserunt fugiat hic eos quaerat voluptas
            distinctio.', 'request': 'Reprehenderit molestiae cupiditate voluptas et voluptatibus illum.'}}, 'opts': 'Et
            vel.', 'type': 'Alias aut voluptas molestiae.'}}

    Attributes:
        account_id (str): Reference to account revenues for this service should be credited to Example:
            cayp:account:acme.
        description (str): More detailed description of the service Example: This service ....
        parameters (List[ParameterDefT]): Service parameter definitions Example: [{'description': 'The name of the
            region as according to ...', 'label': 'Region Name', 'name': 'region', 'type': 'string'}, {'label':
            'Rainfall/month threshold', 'name': 'threshold', 'type': 'float', 'unit': 'm'}].
        provider_id (str): Reference to service provider Example: cayp:provider:acme.
        workflow (WorkflowT): Defines the workflow to use to execute this service. Currently supported 'types' are
            'basic'
                and 'argo'. In case of 'basic', use the 'basic' element for further parameters. In the current implementation
                'opts' is expected to contain the same schema as 'basic' Example: {'argo': 'Nostrum reprehenderit quia.',
            'basic': {'command': ['Unde fuga sed veniam.', 'Et aut autem deserunt sit architecto.', 'Quidem nulla quae
            provident dolor amet nulla.'], 'cpu': {'limit': 'Deserunt fugiat hic eos quaerat voluptas distinctio.',
            'request': 'Reprehenderit molestiae cupiditate voluptas et voluptatibus illum.'}, 'image': 'Officiis consequatur
            corporis autem.', 'memory': {'limit': 'Deserunt fugiat hic eos quaerat voluptas distinctio.', 'request':
            'Reprehenderit molestiae cupiditate voluptas et voluptatibus illum.'}}, 'opts': 'Quae hic dignissimos.', 'type':
            'Commodi dolorem provident ab et.'}.
        banner (Union[Unset, str]): Link to banner image oprionally used for this service Example:
            http://harvey.org/tabitha.
        metadata (Union[Unset, List[ParameterT]]): Optional provider provided meta tags Example: [{'name': 'Odit aut
            quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name': 'Odit aut quod nihil aperiam.',
            'value': 'Ut enim ut fugit possimus pariatur.'}, {'name': 'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut
            fugit possimus pariatur.'}].
        name (Union[Unset, str]): Optional provider provided name Example: Fire risk for Lot2.
        provider_ref (Union[Unset, str]): Provider provided reference. Should to be a single string with punctuations
            allowed. Might be changed, so please check result Example: service_foo_patch_1.
        references (Union[Unset, List[ReferenceT]]): Reference to account revenues for this service should be credited
            to Example: [{'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'}, {'title':
            'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'}].
        tags (Union[Unset, List[str]]): Optional provider provided tags Example: ['tag1', 'tag2'].
    """

    account_id: str
    description: str
    parameters: List[ParameterDefT]
    provider_id: str
    workflow: WorkflowT
    banner: Union[Unset, str] = UNSET
    metadata: Union[Unset, List[ParameterT]] = UNSET
    name: Union[Unset, str] = UNSET
    provider_ref: Union[Unset, str] = UNSET
    references: Union[Unset, List[ReferenceT]] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        description = self.description
        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item = parameters_item_data.to_dict()

            parameters.append(parameters_item)

        provider_id = self.provider_id
        workflow = self.workflow.to_dict()

        banner = self.banner
        metadata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()

                metadata.append(metadata_item)

        name = self.name
        provider_ref = self.provider_ref
        references: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()

                references.append(references_item)

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account-id": account_id,
                "description": description,
                "parameters": parameters,
                "provider-id": provider_id,
                "workflow": workflow,
            }
        )
        if banner is not UNSET:
            field_dict["banner"] = banner
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if provider_ref is not UNSET:
            field_dict["provider-ref"] = provider_ref
        if references is not UNSET:
            field_dict["references"] = references
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account-id")

        description = d.pop("description")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:
            parameters_item = ParameterDefT.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        provider_id = d.pop("provider-id")

        workflow = WorkflowT.from_dict(d.pop("workflow"))

        banner = d.pop("banner", UNSET)

        metadata = []
        _metadata = d.pop("metadata", UNSET)
        for metadata_item_data in _metadata or []:
            metadata_item = ParameterT.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        name = d.pop("name", UNSET)

        provider_ref = d.pop("provider-ref", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = ReferenceT.from_dict(references_item_data)

            references.append(references_item)

        tags = cast(List[str], d.pop("tags", UNSET))

        service_description_t = cls(
            account_id=account_id,
            description=description,
            parameters=parameters,
            provider_id=provider_id,
            workflow=workflow,
            banner=banner,
            metadata=metadata,
            name=name,
            provider_ref=provider_ref,
            references=references,
            tags=tags,
        )

        service_description_t.additional_properties = d
        return service_description_t

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
