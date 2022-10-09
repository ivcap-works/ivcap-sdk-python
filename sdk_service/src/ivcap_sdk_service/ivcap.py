#
# Helper funtions to interface with CSE services
#
import json
from argparse import ArgumentParser
from typing import Callable, Dict

from .logger import logging
from .config import Config, Resource

DELIVERED = []
_CONFIG = None # only use internally and only after calling init()

def deliver(name, data, **meta):
    global DELIVERED

    def xa_dataset(d, name):
        # dm = d.to_dict(data=False)
        # meta = {
        #     "X-": dm
        # }
        fn, url = _CONFIG.IO_ADAPTER.get_fd(f"{name}.nc", d, meta)
        d.to_netcdf(fn, compute=True)
        return url

    switcher = {
        "<class 'xarray.core.dataset.Dataset'>": xa_dataset,
        "<class 'xarray.core.dataarray.DataArray'>": xa_dataset,
    }
    sf = switcher.get(str(type(data)))
    if sf:
        url = sf(data, name)
    else:
        raise NotImplementedError(f"Unsupported data type {type(data)}")

    m = dict(name=name, url=url, type=str(type(data)), meta=meta)
    DELIVERED.append(m)
    notify(m, _CONFIG.SCHEMA_PREFIX + 'deliver')
    return (url, data)


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
        #print(f"... send '{js}'")
        # p.send(CONFIG.KAFKA_CHANNEL, js.encode('utf-8'), headers=h)
        # p.flush()
    else:
        logging.info(f"{schema}: {msg}")

def get_config() -> Config:
    return _CONFIG

def is_valid_resource_urn(urn: str, resource: Resource) -> bool:
    prefix = f"{get_config().SCHEMA_PREFIX}:{resource.value}:"
    #print(f" {prefix} | {urn} |  {urn.startswith(prefix)}")
    return urn.startswith(prefix)

def init(argv:Dict[str, str] = None, modify_ap: Callable[[ArgumentParser], ArgumentParser] = None):
    global _CONFIG
    _CONFIG = Config(argv, modify_ap)
    return _CONFIG

# def init(order_id = None, kafka_server = None, kafka_channel = None):
#   global KAFKA_SERVER, KAFKA_CHANNEL, ORDER_ID
#   if order_id: ORDER_ID = order_id
#   if kafka_server: KAFKA_SERVER = kafka_server
#   if kafka_channel: KAFKA_CHANNEL = kafka_channel

# SUPORT FUNCTIONS
