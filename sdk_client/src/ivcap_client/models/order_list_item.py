from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.order_list_item_status import OrderListItemStatus
from ..models.self_t import SelfT
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderListItem")


@attr.s(auto_attribs=True)
class OrderListItem:
    """
    Example:
        {'account_id': '2022-01-01', 'finished_at': '2022-01-01', 'id':
            'cayp:order:123e4567-e89b-12d3-a456-426614174000', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'},
            'name': 'Fire risk for Lot2', 'ordered_at': '2022-01-01', 'service_id': '2022-01-01', 'status': 'finished'}

    Attributes:
        links (SelfT):  Example: {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Blanditiis necessitatibus animi maiores sed odit.'}.
        account_id (Union[Unset, str]): ID of ordered service Example: 2022-01-01.
        finished_at (Union[Unset, str]): Order Date Example: 2022-01-01.
        id (Union[Unset, str]): Order ID Example: cayp:order:123e4567-e89b-12d3-a456-426614174000.
        name (Union[Unset, str]): Optional customer provided name Example: Fire risk for Lot2.
        ordered_at (Union[Unset, str]): Order Date Example: 2022-01-01.
        service_id (Union[Unset, str]): ID of ordered service Example: 2022-01-01.
        status (Union[Unset, OrderListItemStatus]): Order status Example: pending.
    """

    links: SelfT
    account_id: Union[Unset, str] = UNSET
    finished_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    ordered_at: Union[Unset, str] = UNSET
    service_id: Union[Unset, str] = UNSET
    status: Union[Unset, OrderListItemStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links = self.links.to_dict()

        account_id = self.account_id
        finished_at = self.finished_at
        id = self.id
        name = self.name
        ordered_at = self.ordered_at
        service_id = self.service_id
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
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ordered_at is not UNSET:
            field_dict["ordered_at"] = ordered_at
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        links = SelfT.from_dict(d.pop("links"))

        account_id = d.pop("account_id", UNSET)

        finished_at = d.pop("finished_at", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ordered_at = d.pop("ordered_at", UNSET)

        service_id = d.pop("service_id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderListItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OrderListItemStatus(_status)

        order_list_item = cls(
            links=links,
            account_id=account_id,
            finished_at=finished_at,
            id=id,
            name=name,
            ordered_at=ordered_at,
            service_id=service_id,
            status=status,
        )

        order_list_item.additional_properties = d
        return order_list_item

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
