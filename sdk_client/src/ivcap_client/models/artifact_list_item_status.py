from enum import Enum


class ArtifactListItemStatus(str, Enum):
    BUILDING = "building"
    ERROR = "error"
    PENDING = "pending"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
