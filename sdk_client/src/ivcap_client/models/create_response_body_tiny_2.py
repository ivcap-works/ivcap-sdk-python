from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.self_t import SelfT
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateResponseBodyTiny2")


@attr.s(auto_attribs=True)
class CreateResponseBodyTiny2:
    """CreateResponseBody result type (tiny view)

    Example:
        {'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self':
            'Odio officiis reiciendis.'}, 'name': 'Fire risk for Lot2'}

    Attributes:
        links (SelfT):  Example: {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Blanditiis necessitatibus animi maiores sed odit.'}.
        name (Union[Unset, str]): Optional provider provided name Example: Fire risk for Lot2.
    """

    links: SelfT
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links = self.links.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        links = SelfT.from_dict(d.pop("links"))

        name = d.pop("name", UNSET)

        create_response_body_tiny_2 = cls(
            links=links,
            name=name,
        )

        create_response_body_tiny_2.additional_properties = d
        return create_response_body_tiny_2

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
