from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.self_with_data_t import SelfWithDataT


T = TypeVar("T", bound="ProductT")


@attr.s(auto_attribs=True)
class ProductT:
    """
    Example:
        {'id': 'Aut nostrum maiores deleniti placeat tenetur qui.', 'links': {'data': 'Officiis dolore quo ea.',
            'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self':
            'Perspiciatis cumque quo praesentium.'}, 'mime-type': 'Repellendus vel nulla repellendus eum neque autem.',
            'name': 'Et iusto et magni vitae ut.', 'size': 2047404228262726111, 'status': 'Minus et ad eius commodi non
            pariatur.'}

    Attributes:
        id (Union[Unset, str]):  Example: Fugiat facere quas..
        links (Union[Unset, SelfWithDataT]):  Example: {'data': 'Repellendus atque ad doloremque adipisci atque.',
            'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Iure
            assumenda dolore animi assumenda dolorem eveniet.'}.
        mime_type (Union[Unset, str]):  Example: Animi minus sapiente incidunt quas..
        name (Union[Unset, str]):  Example: Laborum autem delectus..
        size (Union[Unset, int]):  Example: 7775421525677750405.
        status (Union[Unset, str]):  Example: Quo et aut quas..
    """

    id: Union[Unset, str] = UNSET
    links: Union[Unset, "SelfWithDataT"] = UNSET
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
        from ..models.self_with_data_t import SelfWithDataT

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
