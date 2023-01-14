# read version from installed package
from typing import Optional


try:  # Python < 3.10 (backport) 
    from importlib_metadata import version 
except ImportError: 
    from importlib.metadata import version 

try:   
    __version__ = version("ivcap_sdk_service")
except Exception:
    __version__ = "unknown"


from .ivcap import deliver_data, fetch_data, register_saver
from .ivcap import get_config, register_saver, get_order_id, get_node_id
from .run import register_service
from .service import Service, Parameter, Option, Type
from .service import Workflow, BasicWorkflow, PythonWorkflow

from .cio.io_adapter import IOAdapter, OnCloseF, IOWritable, IOReadable
from .itypes import MissingParameterValue, UnsupportedMimeType, SupportedMimeTypes