from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.artifact_status_rt_status import ArtifactStatusRTStatus
from ..models.parameter_t import ParameterT
from ..models.ref_t import RefT
from ..models.self_t import SelfT
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtifactStatusRT")


@attr.s(auto_attribs=True)
class ArtifactStatusRT:
    """
    Example:
        {'account': {'id': 'http://sporer.name/buddy', 'links': {'describedBy': {'href': 'https://api.com/swagger/...',
            'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}, 'collections': ['Excepturi commodi
            autem ad ullam doloremque dolorem.', 'Et cum non.', 'Nemo excepturi ex voluptate corrupti laborum qui.'],
            'data': {'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self':
            'Odio officiis reiciendis.'}, 'id': 'type:scope:name', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'},
            'metadata': [{'name': 'producedBy', 'value': 'https://cre.com/1/orders/000-000'}, {'name': 'createdAt', 'value':
            '2021-07-31T05:25:05'}], 'mime-type': 'Cumque consequatur at est.', 'name': 'Fire risk per LGA', 'size':
            1696992925556432826, 'status': 'complete'}

    Attributes:
        id (str): Artifact ID Example: type:scope:name.
        links (SelfT):  Example: {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Blanditiis necessitatibus animi maiores sed odit.'}.
        status (ArtifactStatusRTStatus): Artifact status Example: pending.
        account (Union[Unset, RefT]):  Example: {'id': 'http://gaylord.biz/jacey', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}.
        collections (Union[Unset, List[str]]): List of collections this artifact is part of Example: ['Ea enim eos
            aliquid.', 'Atque autem quis sint dolorum illo blanditiis.'].
        data (Union[Unset, SelfT]):  Example: {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Blanditiis necessitatibus animi maiores sed odit.'}.
        metadata (Union[Unset, List[ParameterT]]): List of key/value metadata Example: [{'name': 'producedBy', 'value':
            'https://cre.com/1/orders/000-000'}, {'name': 'createdAt', 'value': '2021-07-31T05:25:05'}].
        mime_type (Union[Unset, str]): Mime-type of data Example: Ex facere quo cum veniam..
        name (Union[Unset, str]): Optional name Example: Fire risk per LGA.
        size (Union[Unset, int]): Size of data Example: 4347762301872612951.
    """

    id: str
    links: SelfT
    status: ArtifactStatusRTStatus
    account: Union[Unset, RefT] = UNSET
    collections: Union[Unset, List[str]] = UNSET
    data: Union[Unset, SelfT] = UNSET
    metadata: Union[Unset, List[ParameterT]] = UNSET
    mime_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        links = self.links.to_dict()

        status = self.status.value

        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        collections: Union[Unset, List[str]] = UNSET
        if not isinstance(self.collections, Unset):
            collections = self.collections

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        metadata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()

                metadata.append(metadata_item)

        mime_type = self.mime_type
        name = self.name
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "links": links,
                "status": status,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if collections is not UNSET:
            field_dict["collections"] = collections
        if data is not UNSET:
            field_dict["data"] = data
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if mime_type is not UNSET:
            field_dict["mime-type"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        links = SelfT.from_dict(d.pop("links"))

        status = ArtifactStatusRTStatus(d.pop("status"))

        _account = d.pop("account", UNSET)
        account: Union[Unset, RefT]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = RefT.from_dict(_account)

        collections = cast(List[str], d.pop("collections", UNSET))

        _data = d.pop("data", UNSET)
        data: Union[Unset, SelfT]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SelfT.from_dict(_data)

        metadata = []
        _metadata = d.pop("metadata", UNSET)
        for metadata_item_data in _metadata or []:
            metadata_item = ParameterT.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        mime_type = d.pop("mime-type", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        artifact_status_rt = cls(
            id=id,
            links=links,
            status=status,
            account=account,
            collections=collections,
            data=data,
            metadata=metadata,
            mime_type=mime_type,
            name=name,
            size=size,
        )

        artifact_status_rt.additional_properties = d
        return artifact_status_rt

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
