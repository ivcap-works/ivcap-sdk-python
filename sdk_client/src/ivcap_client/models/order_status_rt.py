from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.order_status_rt_metadata import OrderStatusRTMetadata
from ..models.order_status_rt_status import OrderStatusRTStatus
from ..models.parameter_t import ParameterT
from ..models.product_t import ProductT
from ..models.ref_t import RefT
from ..models.self_t import SelfT
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderStatusRT")


@attr.s(auto_attribs=True)
class OrderStatusRT:
    """
    Example:
        {'account': {'id': 'http://sporer.name/buddy', 'links': {'describedBy': {'href': 'https://api.com/swagger/...',
            'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}, 'id':
            '123e4567-e89b-12d3-a456-426614174000', 'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}, 'metadata': {'refID': '33-444'}, 'name':
            'Fire risk for Lot2', 'ordered_at': '2022-01-01', 'parameters': [{'name': 'region', 'value': 'Upper Valley'},
            {'name': 'threshold', 'value': 10}], 'products': [{'href': 'https:/.../1/artifacts/0000-00001220', 'mime-type':
            'image/geo+tiff', 'name': 'fire risk map', 'size': 1234963}], 'service': {'id': 'http://sporer.name/buddy',
            'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self':
            'Odio officiis reiciendis.'}}, 'status': 'error'}

    Attributes:
        id (str): Order ID Example: 123e4567-e89b-12d3-a456-426614174000.
        parameters (List[ParameterT]): Service parameters Example: [{'name': 'region', 'value': 'Upper Valley'},
            {'name': 'threshold', 'value': 10}].
        account (Union[Unset, RefT]):  Example: {'id': 'http://gaylord.biz/jacey', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}.
        links (Union[Unset, SelfT]):  Example: {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Blanditiis necessitatibus animi maiores sed odit.'}.
        metadata (Union[Unset, OrderStatusRTMetadata]): Optional key/value metadata for reference Example: {'refID':
            '33-444'}.
        name (Union[Unset, str]): Optional customer provided name Example: Fire risk for Lot2.
        ordered_at (Union[Unset, str]): Order Date Example: 2022-01-01.
        products (Union[Unset, List[ProductT]]): Products delivered for this order Example: [{'href':
            'https:/.../1/artifacts/0000-00001220', 'mime-type': 'image/geo+tiff', 'name': 'fire risk map', 'size':
            1234963}].
        service (Union[Unset, RefT]):  Example: {'id': 'http://gaylord.biz/jacey', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}.
        status (Union[Unset, OrderStatusRTStatus]): Order status Example: finished.
    """

    id: str
    parameters: List[ParameterT]
    account: Union[Unset, RefT] = UNSET
    links: Union[Unset, SelfT] = UNSET
    metadata: Union[Unset, OrderStatusRTMetadata] = UNSET
    name: Union[Unset, str] = UNSET
    ordered_at: Union[Unset, str] = UNSET
    products: Union[Unset, List[ProductT]] = UNSET
    service: Union[Unset, RefT] = UNSET
    status: Union[Unset, OrderStatusRTStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item = parameters_item_data.to_dict()

            parameters.append(parameters_item)

        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name
        ordered_at = self.ordered_at
        products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()

                products.append(products_item)

        service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "parameters": parameters,
            }
        )
        if account is not UNSET:
            field_dict["account"] = account
        if links is not UNSET:
            field_dict["links"] = links
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name
        if ordered_at is not UNSET:
            field_dict["ordered_at"] = ordered_at
        if products is not UNSET:
            field_dict["products"] = products
        if service is not UNSET:
            field_dict["service"] = service
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:
            parameters_item = ParameterT.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        _account = d.pop("account", UNSET)
        account: Union[Unset, RefT]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = RefT.from_dict(_account)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SelfT]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SelfT.from_dict(_links)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, OrderStatusRTMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = OrderStatusRTMetadata.from_dict(_metadata)

        name = d.pop("name", UNSET)

        ordered_at = d.pop("ordered_at", UNSET)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = ProductT.from_dict(products_item_data)

            products.append(products_item)

        _service = d.pop("service", UNSET)
        service: Union[Unset, RefT]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = RefT.from_dict(_service)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderStatusRTStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OrderStatusRTStatus(_status)

        order_status_rt = cls(
            id=id,
            parameters=parameters,
            account=account,
            links=links,
            metadata=metadata,
            name=name,
            ordered_at=ordered_at,
            products=products,
            service=service,
            status=status,
        )

        order_status_rt.additional_properties = d
        return order_status_rt

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
