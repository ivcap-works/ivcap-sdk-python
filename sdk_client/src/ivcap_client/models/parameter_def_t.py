from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parameter_opt_t import ParameterOptT


T = TypeVar("T", bound="ParameterDefT")


@attr.s(auto_attribs=True)
class ParameterDefT:
    """
    Example:
        {'constant': False, 'default': 'Corporis consequatur quo ex mollitia eum consequatur.', 'description': 'Iusto
            nihil dolor recusandae.', 'label': 'Unde perferendis recusandae quisquam nostrum et.', 'name': 'Magni nulla
            debitis reiciendis libero.', 'optional': False, 'options': [{'description': 'Fugiat autem corporis omnis.',
            'value': 'Est exercitationem.'}, {'description': 'Fugiat autem corporis omnis.', 'value': 'Est
            exercitationem.'}], 'type': 'Eius fuga beatae blanditiis.', 'unit': 'Aliquam iure vero rerum incidunt commodi.'}

    Attributes:
        constant (Union[Unset, bool]):  Example: True.
        default (Union[Unset, str]):  Example: Qui fugit pariatur numquam omnis similique quisquam..
        description (Union[Unset, str]):  Example: Et beatae laboriosam et accusamus maxime..
        label (Union[Unset, str]):  Example: Qui eum..
        name (Union[Unset, str]):  Example: Eos est vitae quos consequatur..
        optional (Union[Unset, bool]):  Example: True.
        options (Union[Unset, List['ParameterOptT']]):  Example: [{'description': 'Fugiat autem corporis omnis.',
            'value': 'Est exercitationem.'}, {'description': 'Fugiat autem corporis omnis.', 'value': 'Est
            exercitationem.'}].
        type (Union[Unset, str]):  Example: Fuga ipsam quo..
        unit (Union[Unset, str]):  Example: Ea libero..
    """

    constant: Union[Unset, bool] = UNSET
    default: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    optional: Union[Unset, bool] = UNSET
    options: Union[Unset, List["ParameterOptT"]] = UNSET
    type: Union[Unset, str] = UNSET
    unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        constant = self.constant
        default = self.default
        description = self.description
        label = self.label
        name = self.name
        optional = self.optional
        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        type = self.type
        unit = self.unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constant is not UNSET:
            field_dict["constant"] = constant
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if optional is not UNSET:
            field_dict["optional"] = optional
        if options is not UNSET:
            field_dict["options"] = options
        if type is not UNSET:
            field_dict["type"] = type
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parameter_opt_t import ParameterOptT

        d = src_dict.copy()
        constant = d.pop("constant", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        label = d.pop("label", UNSET)

        name = d.pop("name", UNSET)

        optional = d.pop("optional", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = ParameterOptT.from_dict(options_item_data)

            options.append(options_item)

        type = d.pop("type", UNSET)

        unit = d.pop("unit", UNSET)

        parameter_def_t = cls(
            constant=constant,
            default=default,
            description=description,
            label=label,
            name=name,
            optional=optional,
            options=options,
            type=type,
            unit=unit,
        )

        parameter_def_t.additional_properties = d
        return parameter_def_t

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
