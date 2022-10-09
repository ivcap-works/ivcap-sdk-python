
from hashlib import sha256
import re
import shutil
import requests
from pathlib import Path

from ..logger import logger
from .file_adapter import FileAdapter

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
        self.cacheIO = FileAdapter(
            in_dir=cache_dir,
            out_dir=cache_dir
        )
        self.url_mapper = url_mapper

    def get_file_path(self, url: str) -> str:
        path = self.url2path.get(url)
        if not path:
            cname = get_cache_name(url)
            # TODO: corrupted download?
            (exists,path) = self.cacheIO.exists(cname)
            if not exists:
                path = self.download_file(url, cname)
            else:
                logger.debug(f"Found '{url}' in local cache ({path})")
            self.url2path[url] = path
        return path

    def download_file(self, url, cname):
        (fh, path) = self.cacheIO.get_fd(cname)
        url = self.url_mapper(url)
        logger.debug(f"Downloading {url} to cache {path}")
        with requests.get(url, stream=True) as r:
            shutil.copyfileobj(r.raw, fh)
        fh.close()
        return path


def get_cache_name(url):
    name = re.search('.*/([^/]+)', url)[1]
    encoded_name = f"{sha256(url.encode('utf-8')).hexdigest()}-{name}"
    return encoded_name

