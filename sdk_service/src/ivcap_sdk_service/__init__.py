# read version from installed package
try:  # Python < 3.10 (backport) 
    from importlib_metadata import version 
except ImportError: 
    from importlib.metadata import version 

try:   
    __version__ = version("ivcap_sdk_service")
except Exception:
    __version__ = "unknown"
    
from .ivcap import get_config, deliver_data, fetch_data
from .run import run, register_service
from .service import Service, Parameter, Option, Type
from .service import Workflow, BasicWorkflow, PythonWorkflow

#from cayp.cayp import *
