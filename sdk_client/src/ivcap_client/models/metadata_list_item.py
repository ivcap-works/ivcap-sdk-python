from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="MetadataListItem")


@attr.s(auto_attribs=True)
class MetadataListItem:
    """
    Example:
        {'entity-id': 'urn:blue:transect.1', 'metadata': '{...}', 'record-id':
            'urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000', 'schema': 'urn:blue:image'}

    Attributes:
        entity_id (Union[Unset, str]): Entity ID Example: urn:blue:transect.1.
        metadata (Union[Unset, File]): Attached metadata Example: {...}.
        record_id (Union[Unset, str]): Record ID Example: urn:ivcap:record.123e4567-e89b-12d3-a456-426614174000.
        schema (Union[Unset, str]): Schema ID Example: urn:blue:image.
    """

    entity_id: Union[Unset, str] = UNSET
    metadata: Union[Unset, File] = UNSET
    record_id: Union[Unset, str] = UNSET
    schema: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        metadata: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_tuple()

        record_id = self.record_id
        schema = self.schema

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entity-id"] = entity_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if record_id is not UNSET:
            field_dict["record-id"] = record_id
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entity_id = d.pop("entity-id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, File]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = File(payload=BytesIO(_metadata))

        record_id = d.pop("record-id", UNSET)

        schema = d.pop("schema", UNSET)

        metadata_list_item = cls(
            entity_id=entity_id,
            metadata=metadata,
            record_id=record_id,
            schema=schema,
        )

        metadata_list_item.additional_properties = d
        return metadata_list_item

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
