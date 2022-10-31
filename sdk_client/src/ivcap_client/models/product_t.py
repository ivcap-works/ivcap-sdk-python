from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.self_with_data_t import SelfWithDataT
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductT")


@attr.s(auto_attribs=True)
class ProductT:
    """
    Example:
        {'id': 'Voluptatem assumenda natus reiciendis voluptatem.', 'links': {'data': 'Necessitatibus velit quia odit
            earum adipisci.', 'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'},
            'self': 'Inventore sint.'}, 'mime-type': 'Tempora illum vel.', 'name': 'Ea officiis.', 'size':
            7149585304102376231, 'status': 'Vitae aspernatur aliquid sed rerum.'}

    Attributes:
        id (Union[Unset, str]):  Example: Autem est..
        links (Union[Unset, SelfWithDataT]):  Example: {'data': 'Est qui est reprehenderit est accusantium ipsa.',
            'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Quis
            fuga.'}.
        mime_type (Union[Unset, str]):  Example: Et ab facere deserunt sapiente..
        name (Union[Unset, str]):  Example: Dolor nostrum eveniet..
        size (Union[Unset, int]):  Example: 210834397676315722.
        status (Union[Unset, str]):  Example: Eius similique..
    """

    id: Union[Unset, str] = UNSET
    links: Union[Unset, SelfWithDataT] = UNSET
    mime_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        mime_type = self.mime_type
        name = self.name
        size = self.size
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if mime_type is not UNSET:
            field_dict["mime-type"] = mime_type
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfWithDataT]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfWithDataT.from_dict(_links)

        mime_type = d.pop("mime-type", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        status = d.pop("status", UNSET)

        product_t = cls(
            id=id,
            links=links,
            mime_type=mime_type,
            name=name,
            size=size,
            status=status,
        )

        product_t.additional_properties = d
        return product_t

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
