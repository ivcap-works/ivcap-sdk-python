from enum import Enum


class CreateResponseBodyTinyStatus(str, Enum):
    PENDING = "pending"
    EXECUTING = "executing"
    FINISHED = "finished"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
