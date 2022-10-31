from enum import Enum


class ServiceStatusRTStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
