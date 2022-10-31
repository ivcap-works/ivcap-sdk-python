from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.artifact_list_item_status import ArtifactListItemStatus
from ..models.self_t import SelfT
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtifactListItem")


@attr.s(auto_attribs=True)
class ArtifactListItem:
    """
    Example:
        {'id': 'cayp:artifact:0000-000', 'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}, 'name': 'Fire risk for Lot2', 'status':
            'ready'}

    Attributes:
        links (SelfT):  Example: {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Blanditiis necessitatibus animi maiores sed odit.'}.
        id (Union[Unset, str]): Artifact ID Example: cayp:artifact:0000-000.
        name (Union[Unset, str]): Optional name Example: Fire risk for Lot2.
        status (Union[Unset, ArtifactListItemStatus]): Artifact status Example: ready.
    """

    links: SelfT
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, ArtifactListItemStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links = self.links.to_dict()

        id = self.id
        name = self.name
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        links = SelfT.from_dict(d.pop("links"))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ArtifactListItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ArtifactListItemStatus(_status)

        artifact_list_item = cls(
            links=links,
            id=id,
            name=name,
            status=status,
        )

        artifact_list_item.additional_properties = d
        return artifact_list_item

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
