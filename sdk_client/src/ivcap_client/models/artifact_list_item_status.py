from enum import Enum


class ArtifactListItemStatus(str, Enum):
    PENDING = "pending"
    BUILDING = "building"
    READY = "ready"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
