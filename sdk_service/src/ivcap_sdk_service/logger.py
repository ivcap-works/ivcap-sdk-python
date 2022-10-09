
import logging

# format
_level = 'DEBUG'
_format = '%(asctime)s %(name)s %(levelname)s %(message)s'
_datefmt = '%Y-%m-%dT%H:%M:%S%z'
logging.basicConfig(level=_level, format=_format, datefmt=_datefmt)

logger = logging.getLogger("service")
sys_logger = logging.getLogger("system")