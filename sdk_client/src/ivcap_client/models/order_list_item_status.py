from enum import Enum


class OrderListItemStatus(str, Enum):
    PENDING = "pending"
    EXECUTING = "executing"
    FINISHED = "finished"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
