from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NavT")


@attr.s(auto_attribs=True)
class NavT:
    """
    Example:
        {'first': 'https://api.com/foo/...', 'next': 'https://api.com/foo/...', 'self': 'https://api.com/foo/...'}

    Attributes:
        first (Union[Unset, str]):  Example: https://api.com/foo/....
        next_ (Union[Unset, str]):  Example: https://api.com/foo/....
        self_ (Union[Unset, str]):  Example: https://api.com/foo/....
    """

    first: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    self_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first = self.first
        next_ = self.next_
        self_ = self.self_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first is not UNSET:
            field_dict["first"] = first
        if next_ is not UNSET:
            field_dict["next"] = next_
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first = d.pop("first", UNSET)

        next_ = d.pop("next", UNSET)

        self_ = d.pop("self", UNSET)

        nav_t = cls(
            first=first,
            next_=next_,
            self_=self_,
        )

        nav_t.additional_properties = d
        return nav_t

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
