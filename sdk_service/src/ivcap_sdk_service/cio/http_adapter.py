#
# Copyright (c) 2023 Commonwealth Scientific and Industrial Research Organisation (CSIRO). All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file. See the AUTHORS file for names of contributors.
#

"""
PostAdapter a wrapper around io.IOBase that sets a http storage backend
"""
import sys
import io
from urllib.parse import urlparse
from typing import Tuple, BinaryIO, Dict
import requests
from ..logger import sys_logger as logger
from .io_adapter import IOAdapter, IOReadable
from .writable_proxy_file import WritableProxyFile
#from .file_adapter import FileProxy
from .cache import Cache
import base64


def meta_xarray(ds: any) -> Tuple[str, Dict[str, any]]:
    dataset_metadata = ds.to_dict(data=False)
    return ("urn:schema:xarray", dataset_metadata)

type2mime = {
    "<class 'xarray.core.dataset.Dataset'>": "application/netcdf",
    "<class 'xarray.core.dataarray.DataArray'>": "application/netcdf",
}

type2meta = {
    "<class 'xarray.core.dataset.Dataset'>": meta_xarray,
    "<class 'xarray.core.dataarray.DataArray'>": meta_xarray,
}

# class PostableProxyFile(WritableProxyFile):
#     """
#     A class which implements the io.IOBase interface for writing data. It additionally
#     persists the data locally for files which require a seekable file object

#     Attributes
#     ----------
#     name : str
#         Name of the data object
#     url : str
#         URL to post content to.

#     """

#     def __init__(self, name: str, url: str, dataPeek: any, meta: Dict[str, any] = {}):
#         super().__init__(name)
#         self.url = url
#         self.dataPeek = dataPeek
#         self.meta = meta

#     def _upload(self):
#         self.file_obj.flush()
#         self.file_obj.seek(0)

#         dataType = str(type(self.dataPeek))
#         ct = type2mime.get(dataType, "unknown")
#         headers = {
#             "X-Name": self.name,
#             "Content-Type": ct,
#         }
#         if len(self.meta):
#             headers['Upload-Metadata'] = ','. join(map(lambda e: f"{e[0]} {encode64(str(e[1]))}", self.meta.items()))
#         try:
#             r = requests.post(self.url, data=self.file_obj, headers=headers)
#             logger.debug(f"WritableProxyFile: wrote file {self.url} response: {r}")
#         except:
#             logger.fatal(f"while posting result data {self.url} - {sys.exc_info()[0]}")
#             sys.exit(-1)
#         if r.status_code >= 300:
#             logger.fatal(f"error response {r.status_code} while posting result data {self.url}")
#             sys.exit(-1)

#         mf = type2meta.get(dataType)
#         if mf:
#             (schema, md) = mf(self.dataPeek)
#             headers = {
#                 "X-Meta-Data-For-Url": self.url,
#                 "X-Meta-Data-For-Id": r.headers.get("X-Artifact-Id", "???"),
#                 "X-Meta-Data-Schema": schema,
#             }
#             u = urlparse(self.url)
#             p = f"{u.path.replace('.', '-')}-meta.json"
#             murl = u._replace(path=p).geturl()
#             try: 
#                 r = requests.post(murl, json=md, headers=headers)
#                 logger.debug(f"WritableProxyFile: write metadata file {murl} response: {r}")
#                 if r.status_code >= 300:
#                     logger.fatal(f"error response {r.status_code} while posting metadata data {murl}")
#             except:
#                 logger.error(f"while posting metadata {self.url} - {sys.exc_info()[0]}")

class HttpAdapter(IOAdapter):
    """
    An adapter for a remote http backend.

    Attributes
    ----------
    storageURL : str
        Name of the order, set via Config/API
    orderID: str
        Path for input data, set via Config/API

    Methods
    -------
    get_fd(name='filename.txt')
        Return an open file handle and path to file
    """
    def __init__(self, storage_url: str, cache: Cache, order_id: str) -> None:
        super().__init__()
        self.storageURL = storage_url
        self.cache = cache
        self.orderID = order_id

    # def get_fd(self, name: str, dataPeek: any = None, meta: Dict[str, any] = {}) -> Tuple[BinaryIO, str]:
    #     url = f"{self.storageURL}/{name}"
    #     f = PostableProxyFile(name, url, dataPeek, meta)
    #     return (f, url)

    def exists(self, name: str) -> Tuple[bool, str]:
        return (False, name)

    def readable(self, name: str) -> bool:
        return True # Note: FIX ME

    def read(self, name: str, seekable=False, use_cache_proxy=True) -> IOReadable:
        logger.debug(f"HttpAdapter: read '{name}'")
        fname = self.cache.download_file(name, None, use_cache_proxy=use_cache_proxy)
        return FileProxy(fname)


def encode64(s: str) -> str:
    sb = s.encode('ascii')
    ba = base64.b64encode(sb)
    return ba.decode('ascii')
