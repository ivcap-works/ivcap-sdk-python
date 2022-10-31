from enum import Enum


class ArtifactStatusRTStatus(str, Enum):
    PENDING = "pending"
    COMPLETE = "complete"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
