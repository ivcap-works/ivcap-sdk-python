from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.artifact_list_item import ArtifactListItem
from ..models.nav_t import NavT

T = TypeVar("T", bound="ArtifactListRT")


@attr.s(auto_attribs=True)
class ArtifactListRT:
    """
    Example:
        {'artifacts': [{'id': 'cayp:artifact:0000-000', 'links': {'describedBy': {'href': 'https://api.com/swagger/...',
            'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'}, 'name': 'Fire risk for Lot2',
            'status': 'ready'}, {'id': 'cayp:artifact:0000-000', 'links': {'describedBy': {'href':
            'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis reiciendis.'},
            'name': 'Fire risk for Lot2', 'status': 'ready'}, {'id': 'cayp:artifact:0000-000', 'links': {'describedBy':
            {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio officiis
            reiciendis.'}, 'name': 'Fire risk for Lot2', 'status': 'ready'}], 'links': {'first': 'https://api.com/foo/...',
            'next': 'https://api.com/foo/...', 'self': 'https://api.com/foo/...'}}

    Attributes:
        artifacts (List[ArtifactListItem]): Artifacts Example: [{'id': 'cayp:artifact:0000-000', 'links':
            {'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self': 'Odio
            officiis reiciendis.'}, 'name': 'Fire risk for Lot2', 'status': 'ready'}, {'id': 'cayp:artifact:0000-000',
            'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self':
            'Odio officiis reiciendis.'}, 'name': 'Fire risk for Lot2', 'status': 'ready'}, {'id': 'cayp:artifact:0000-000',
            'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self':
            'Odio officiis reiciendis.'}, 'name': 'Fire risk for Lot2', 'status': 'ready'}, {'id': 'cayp:artifact:0000-000',
            'links': {'describedBy': {'href': 'https://api.com/swagger/...', 'type': 'application/openapi3+json'}, 'self':
            'Odio officiis reiciendis.'}, 'name': 'Fire risk for Lot2', 'status': 'ready'}].
        links (NavT):  Example: {'first': 'https://api.com/foo/...', 'next': 'https://api.com/foo/...', 'self':
            'https://api.com/foo/...'}.
    """

    artifacts: List[ArtifactListItem]
    links: NavT
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artifacts = []
        for artifacts_item_data in self.artifacts:
            artifacts_item = artifacts_item_data.to_dict()

            artifacts.append(artifacts_item)

        links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artifacts": artifacts,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        artifacts = []
        _artifacts = d.pop("artifacts")
        for artifacts_item_data in _artifacts:
            artifacts_item = ArtifactListItem.from_dict(artifacts_item_data)

            artifacts.append(artifacts_item)

        links = NavT.from_dict(d.pop("links"))

        artifact_list_rt = cls(
            artifacts=artifacts,
            links=links,
        )

        artifact_list_rt.additional_properties = d
        return artifact_list_rt

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
