from enum import Enum


class ArtifactStatusRTStatus(str, Enum):
    COMPLETE = "complete"
    ERROR = "error"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
