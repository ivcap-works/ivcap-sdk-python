from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidParameterValue")


@attr.s(auto_attribs=True)
class InvalidParameterValue:
    """Invalide parameter value

    Example:
        {'message': 'Doloremque dolorem facilis et.', 'name': 'Non et nemo excepturi ex.', 'value': 'Corrupti laborum
            qui incidunt.'}

    Attributes:
        message (str): message describing expected type or pattern. Example: Ut sint dolorum qui corrupti..
        name (str): name of parameter. Example: Aut accusantium quo suscipit ducimus fugiat..
        value (Union[Unset, str]): provided parameter value. Example: Dolorem pariatur repudiandae excepturi commodi
            autem ad..
    """

    message: str
    name: str
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        name = self.name
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "name": name,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message")

        name = d.pop("name")

        value = d.pop("value", UNSET)

        invalid_parameter_value = cls(
            message=message,
            name=name,
            value=value,
        )

        invalid_parameter_value.additional_properties = d
        return invalid_parameter_value

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
