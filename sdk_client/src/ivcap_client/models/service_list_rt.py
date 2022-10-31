from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.nav_t import NavT
from ..models.service_list_item import ServiceListItem

T = TypeVar("T", bound="ServiceListRT")


@attr.s(auto_attribs=True)
class ServiceListRT:
    """
    Example:
        {'links': {'first': 'https://api.com/foo/...', 'next': 'https://api.com/foo/...', 'self':
            'https://api.com/foo/...'}, 'services': [{'description': 'Some lengthy description of fire risk', 'id':
            'service:acme:oracle', 'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}, 'name': 'Fire risk for region', 'provider':
            {'id': 'http://sporer.name/buddy', 'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}}, {'description': 'Some lengthy description
            of fire risk', 'id': 'service:acme:oracle', 'links': {'describedBy': {'href': 'https://api.com/swagger/...',
            'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}, 'name': 'Fire risk for region',
            'provider': {'id': 'http://sporer.name/buddy', 'links': {'describedBy': {'href': 'https://api.com/swagger/...',
            'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}}, {'description': 'Some lengthy
            description of fire risk', 'id': 'service:acme:oracle', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'},
            'name': 'Fire risk for region', 'provider': {'id': 'http://sporer.name/buddy', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}}]}

    Attributes:
        links (NavT):  Example: {'first': 'https://api.com/foo/...', 'next': 'https://api.com/foo/...', 'self':
            'https://api.com/foo/...'}.
        services (List[ServiceListItem]): Services Example: [{'description': 'Some lengthy description of fire risk',
            'id': 'service:acme:oracle', 'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}, 'name': 'Fire risk for region', 'provider':
            {'id': 'http://sporer.name/buddy', 'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type':
            'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}}, {'description': 'Some lengthy description
            of fire risk', 'id': 'service:acme:oracle', 'links': {'describedBy': {'href': 'https://api.com/swagger/...',
            'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}, 'name': 'Fire risk for region',
            'provider': {'id': 'http://sporer.name/buddy', 'links': {'describedBy': {'href': 'https://api.com/swagger/...',
            'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}}, {'description': 'Some lengthy
            description of fire risk', 'id': 'service:acme:oracle', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'},
            'name': 'Fire risk for region', 'provider': {'id': 'http://sporer.name/buddy', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}}},
            {'description': 'Some lengthy description of fire risk', 'id': 'service:acme:oracle', 'links': {'describedBy':
            {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis
            reiciendis.'}, 'name': 'Fire risk for region', 'provider': {'id': 'http://sporer.name/buddy', 'links':
            {'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio
            officiis reiciendis.'}}}].
    """

    links: NavT
    services: List[ServiceListItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links = self.links.to_dict()

        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()

            services.append(services_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
                "services": services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        links = NavT.from_dict(d.pop("links"))

        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = ServiceListItem.from_dict(services_item_data)

            services.append(services_item)

        service_list_rt = cls(
            links=links,
            services=services,
        )

        service_list_rt.additional_properties = d
        return service_list_rt

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
