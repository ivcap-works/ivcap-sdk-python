# read version from installed package
try:  # Python < 3.10 (backport) 
    from importlib_metadata import version 
except ImportError: 
    from importlib.metadata import version 
     
__version__ = version("ivcap_service")

from .ivcap import get_config
from .run import run, register_service
from .service import Service, Parameter, Option, Type

#from cayp.cayp import *
