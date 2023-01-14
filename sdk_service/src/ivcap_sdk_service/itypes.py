from enum import Enum
from typing import Dict, Any, Optional, Union, Callable
from numbers import Number
#from .cio import IOAdapter

class SupportedMimeTypes(Enum):
    NETCDF = 'application/netcdf'
    PNG = 'image/png'
    JPEG = 'image/jpeg'


# type
Url = str
MetaDict = Dict[str, Union[str, Number, bool]]
FilePath = str

class MissingParameterValue(Exception): 
    name: str
    message: Optional[str]

    def __init__(self, name: str, message:str = None):
        self.name = name
        self.message = message

class UnsupportedMimeType(Exception): 
    mime_type: str

    def __init__(self, mime_type: str):
        self.mime_type = mime_type

