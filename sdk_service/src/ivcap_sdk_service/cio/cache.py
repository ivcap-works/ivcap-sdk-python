
from hashlib import sha256
import re
import uuid
import requests
from pathlib import Path

from ..itypes import Url
from ..logger import sys_logger as logger

from .io_adapter import IOReadable


class Cache():
    """
    An adapter for a standard file system backend.

    Attributes
    ----------
    in_dir: str
        Path for input data, set via Config/API
    out_dir: str
        Path for output data, set via Config/API

    Methods
    -------
    get_fd(name='filename.txt')
        Return an open file handle and path to file
    exists(name='filename.txt')
        Check if filename exists
    """
    def __init__(self, cache_dir: str, url_mapper) -> None:
        self.url2path = {}
        Path(cache_dir).mkdir(parents=True, exist_ok=True)
        from .local_io_adapter import LocalIOAdapter # avoid circular dependencies
        self.cacheIO = LocalIOAdapter(
            in_dir=cache_dir,
            out_dir=cache_dir
        )
        self.url_mapper = url_mapper
        self._cache_dir = cache_dir

    def get_and_cache_file(self, url: Url) -> IOReadable:
        cname = get_cache_name(url)
        if self.cacheIO.readable_local(cname):
            logger.debug("Cache#get_and_cache_file: Hit! '%s' already cached as '%s'", url, cname)
            return self.cacheIO.read_local(cname)
        else:
            logger.debug("Cache#get_and_cache_file: Cache '%s' locally as '%s'", url, cname)
            return self.cacheIO.read_external(url, local_file_name=cname)

    #     cpath = os.path.join(prefix, cname)
    #     # TODO: corrupted download?
    #     (exists,path) = self.cacheIO.exists(cname)
    #     if not exists:
    #         path = self.download_file(url, cname)
    #     else:
    #         logger.debug(f"Found '{url}' in local cache ({path})")
    #     self.url2path[url] = path
    # return path        

    # def get_file_path(self, url: str) -> str:
    #     path = self.url2path.get(url)
    #     if not path:
    #         cname = get_cache_name(url)
    #         # TODO: corrupted download?
    #         (exists,path) = self.cacheIO.exists(cname)
    #         if not exists:
    #             path = self.download_file(url, cname)
    #         else:
    #             logger.debug(f"Found '{url}' in local cache ({path})")
    #         self.url2path[url] = path
    #     return path

    # def download_file(self, url, cname=None, use_cache_proxy=True) -> str:
    #     if not cname:
    #         cname = str(uuid.uuid5(uuid.NAMESPACE_DNS, url))
    #     if use_cache_proxy:
    #         url = self.url_mapper(url)
    #     # with requests.get(url, stream=True) as r:
    #     #     logger.info(f"request {r}")
    #     #     shutil.copyfileobj(r.raw, fh)
    #     with requests.get(url, stream=True) as r:
    #         r.raise_for_status()
    #         ct = r.headers.get('Content-Type')
    #         logger.info(f"request {r} - {ct} - {r.headers}")

    #         if ct:
    #             cname = f"{cname}.{ct.replace('/', '.')}"
    #         (fh, path) = self.cacheIO.get_fd(cname)
    #         logger.info(f"Downloading {url} to cache {path}")

    #         for chunk in r.iter_content(chunk_size=None): # 8192): 
    #             #logger.info(f"chunk {chunk}")
    #             # If you have chunk encoded response uncomment if
    #             # and set chunk_size parameter to None.
    #             #if chunk: 
    #             fh.write(chunk)            
    #         fh.close()
    #     logger.info(f"finished downloading {url} to cache {path}")
    #     return path

    def __repr__(self):
        return f"<Cache cache_dir={self._cache_dir}>"


def get_cache_name(url: Url) -> str:
    name = re.search('.*/([^/]+)', url)[1]
    encoded_name = f"{sha256(url.encode('utf-8')).hexdigest()}-{name}"
    return encoded_name

