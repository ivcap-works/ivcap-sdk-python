from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.order_request_t_metadata import OrderRequestTMetadata
from ..models.parameter_t import ParameterT
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderRequestT")


@attr.s(auto_attribs=True)
class OrderRequestT:
    """
    Example:
        {'accountID': '123e4567-e89b-12d3-a456-426614174000', 'metadata': {'refID': '33-444'}, 'name': 'Fire risk for
            Lot2', 'parameters': [{'name': 'region', 'value': 'Upper Valley'}, {'name': 'threshold', 'value': 10}],
            'serviceID': '123e4567-e89b-12d3-a456-426614174000'}

    Attributes:
        account_id (str): Reference to billable account Example: 123e4567-e89b-12d3-a456-426614174000.
        parameters (List[ParameterT]): Service parameters Example: [{'name': 'region', 'value': 'Upper Valley'},
            {'name': 'threshold', 'value': 10}].
        service_id (str): Reference to service requested Example: 123e4567-e89b-12d3-a456-426614174000.
        metadata (Union[Unset, OrderRequestTMetadata]): Optional key/value metadata for reference Example: {'refID':
            '33-444'}.
        name (Union[Unset, str]): Optional customer provided name Example: Fire risk for Lot2.
    """

    account_id: str
    parameters: List[ParameterT]
    service_id: str
    metadata: Union[Unset, OrderRequestTMetadata] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item = parameters_item_data.to_dict()

            parameters.append(parameters_item)

        service_id = self.service_id
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountID": account_id,
                "parameters": parameters,
                "serviceID": service_id,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountID")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:
            parameters_item = ParameterT.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        service_id = d.pop("serviceID")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OrderRequestTMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OrderRequestTMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        order_request_t = cls(
            account_id=account_id,
            parameters=parameters,
            service_id=service_id,
            metadata=metadata,
            name=name,
        )

        order_request_t.additional_properties = d
        return order_request_t

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
