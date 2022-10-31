from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.metadata_list_item import MetadataListItem
from ..models.nav_t import NavT

T = TypeVar("T", bound="ReadMetaRT")


@attr.s(auto_attribs=True)
class ReadMetaRT:
    """
    Example:
        {'links': {'first': 'https://api.com/foo/...', 'next': 'https://api.com/foo/...', 'self':
            'https://api.com/foo/...'}, 'records': [{'entity-id': 'urn:blue:transect.1', 'metadata': '{...}', 'record-id':
            'urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000', 'schema': 'urn:blue:image'}, {'entity-id':
            'urn:blue:transect.1', 'metadata': '{...}', 'record-id':
            'urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000', 'schema': 'urn:blue:image'}, {'entity-id':
            'urn:blue:transect.1', 'metadata': '{...}', 'record-id':
            'urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000', 'schema': 'urn:blue:image'}, {'entity-id':
            'urn:blue:transect.1', 'metadata': '{...}', 'record-id':
            'urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000', 'schema': 'urn:blue:image'}]}

    Attributes:
        links (NavT):  Example: {'first': 'https://api.com/foo/...', 'next': 'https://api.com/foo/...', 'self':
            'https://api.com/foo/...'}.
        records (List[MetadataListItem]): List of metadata records Example: [{'entity-id': 'urn:blue:transect.1',
            'metadata': '{...}', 'record-id': 'urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000', 'schema':
            'urn:blue:image'}, {'entity-id': 'urn:blue:transect.1', 'metadata': '{...}', 'record-id':
            'urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000', 'schema': 'urn:blue:image'}, {'entity-id':
            'urn:blue:transect.1', 'metadata': '{...}', 'record-id':
            'urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000', 'schema': 'urn:blue:image'}].
    """

    links: NavT
    records: List[MetadataListItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links = self.links.to_dict()

        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()

            records.append(records_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "links": links,
                "records": records,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        links = NavT.from_dict(d.pop("links"))

        records = []
        _records = d.pop("records")
        for records_item_data in _records:
            records_item = MetadataListItem.from_dict(records_item_data)

            records.append(records_item)

        read_meta_rt = cls(
            links=links,
            records=records,
        )

        read_meta_rt.additional_properties = d
        return read_meta_rt

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
