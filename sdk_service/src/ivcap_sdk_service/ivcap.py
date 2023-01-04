#
# Helper funtions to interface with CSE services
#
import json
from argparse import ArgumentParser
from typing import BinaryIO, Callable, Dict, Any, Optional, Union
from numbers import Number

from .cio.io_adapter import IOReadable

from .logger import sys_logger as logger
from .config import Config, Resource

DELIVERED = []
_CONFIG = None # only use internally and only after calling init()

def xa_dataset(d, name, meta):
    fhdl, url = _CONFIG.IO_ADAPTER.get_fd(f"{name}.nc", d, meta)
    d.to_netcdf(fhdl, compute=True)
    return url

_SAVER = {
    "<class 'xarray.core.dataset.Dataset'>": xa_dataset,
    "<class 'xarray.core.dataarray.DataArray'>": xa_dataset,
}

Url = str
MetaDict = Dict[str, Union[str, Number, bool]]
FilePath = str

def deliver_data(name: str, 
            data_or_lambda: Union[Any, Callable[[BinaryIO], None]],
            data_type: Optional[str] = None,
            meta: Optional[MetaDict] = {}
    ) -> Url:
    """Deliver the result of a service

    Args:
        name (str): _description_
        data_or_lambda (Union[Any, Callable[[BinaryIO], None]]): The data to deliver. Either directly or a callback 
            providing a file-like handle to provide the data then.
        data_type (Optional[str], optional): Data type to save. If not provided `str(type(data)` is used. Defaults to None.
        meta (Optional[MetaDict], optional): Optional metadata to be attached to 'data' . Defaults to {}.

    Raises:
        NotImplementedError: Raised when no saver function is defined for 'type'

    Returns:
        Url: Url under which data was delivered to
    """

    global DELIVERED

    if callable(data_or_lambda):
        l = data_or_lambda
        fhdl, url = _CONFIG.IO_ADAPTER.get_fd(name, None, meta)
        type_s = data_type if data_type else 'unknown'
        l(fhdl)
        fhdl.close()
    else: 
        data = data_or_lambda
        type_s = data_type if data_type else str(type(data))
        sf = _SAVER.get(type_s)
        if sf:
            url = sf(data, name, meta)
        else:
            raise NotImplementedError(f"Unsupported data type {type(data)}")

    m = dict(name=name, url=url, type=type_s, meta=meta)
    DELIVERED.append(m)
    notify(m, _CONFIG.SCHEMA_PREFIX + ':deliver')
    return url

def register_saver(type: Any, f: Callable[[Any, str, MetaDict], Url]):
    """Register a 'saver' function used in 'deliver' for a specific data type.

    Args:
        type (Any): Type identifier
        f (Callable[[data:Any, name:str, meta:MetaDict], Url]): Function to save data and metadata and return URL used
    """
    _SAVER[str(type)] = f

def fetch_data(url: Url, cache: bool = True) -> IOReadable:
    return _CONFIG.IO_ADAPTER.read(url, cache)
    # if cache and _CONFIG.CACHE != None:
    #     return _CONFIG.CACHE.get_file_path(url)
    # else 
    #     return _CONFIG.IO_ADAPTER.get_fd(url)

def cache_file(url):
    if _CONFIG.CACHE != None:
        return _CONFIG.CACHE.get_file_path(url)
    return cachable_url(url)


def get_order_id():
    """Returns the ID of the currently processed order"""
    return _CONFIG.ORDER_ID


def get_node_id():
    """Returns the ID of this computational entity"""
    return _CONFIG.NODE_ID

class ExitException(Exception):
    def __init__(self, msg):
        self.msg = msg
            

def notify(msg, schema=None):
    """Publish 'msg' to indicate progress."""
    p = False # _get_kafka_producer()
    if p:
        h = [
            ('Content-Type', b'application/json'),
            ('CAYP-Order-ID', get_order_id().encode("UTF-8")),
            ('CAYP-Node-ID', get_node_id().encode("UTF-8"))
        ]
        if schema:
            h.append(('Content-Schema', schema.encode('utf-8')))

        js = json.dumps(msg)
        # this is a bit of a hack, but ...
        if (js.startswith('{')):
            extra = {'@order_id': get_order_id(), '@node_id': get_node_id()}
            if schema:
                extra['@schema'] = schema
            jx = json.dumps(extra)
            js = f"{js[0]}{jx[1:-1]},{js[1:]}"
    else:
        logger.info(f"{schema}: {msg}")

def get_config() -> Config:
    return _CONFIG

def is_valid_resource_urn(urn: str, resource: Resource) -> bool:
    prefix = f"{get_config().SCHEMA_PREFIX}:{resource.value}:"
    return urn.startswith(prefix)

def init(argv:Dict[str, str] = None, modify_ap: Callable[[ArgumentParser], ArgumentParser] = None):
    global _CONFIG
    _CONFIG = Config(argv, modify_ap)
    return _CONFIG

# SUPORT FUNCTIONS
