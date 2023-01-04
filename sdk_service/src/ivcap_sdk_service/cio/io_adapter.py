from abc import ABC, abstractmethod
from typing import AnyStr, List, Tuple, Union, BinaryIO, Dict
import tempfile
import io
import shutil
from ..logger import logger

class _IOBase(ABC):
    @property
    @abstractmethod
    def mode(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @property
    @abstractmethod
    def closed(self) -> bool:
        pass

    @abstractmethod
    def readable(self) -> bool:
        pass


    @abstractmethod
    def seek(self, offset: int, whence: int = 0) -> int:
        pass

    @abstractmethod
    def seekable(self) -> bool:
        pass

    @abstractmethod
    def tell(self) -> int:
        pass

    @abstractmethod
    def truncate(self, size: int = None) -> int:
        pass

    @abstractmethod
    def writable(self) -> bool:
        pass

class IOReadable(_IOBase):
    @abstractmethod
    def read(self, n: int = -1) -> AnyStr:
        pass

    @abstractmethod
    def readline(self, limit: int = -1) -> AnyStr:
        pass

    @abstractmethod
    def readlines(self, hint: int = -1) -> List[AnyStr]:
        pass

class IOWritable(_IOBase):
    @abstractmethod
    def write(self, s: AnyStr) -> int:
        pass

    @abstractmethod
    def writelines(self, lines: List[AnyStr]) -> None:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass


class IO_ReadWritable(IOReadable, IOWritable):
    pass


class IOProxy(ABC):
    """Represents a file-like object to read and write to"""

    @abstractmethod
    def open(self, mode: str, **kwargs) -> IO_ReadWritable:
        """Return an IO object to read or write to depending on 'mode'"""

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def name(self) -> str:
        """Returns name of underlying object"""
        pass

        
class IOAdapter(ABC):

    def create_cache(cls, cacheDir: str, cache_proxy_url: str):
        #return Cache(cache_dir=cacheDir, url_mapper=urlMapper)
        return None

    @abstractmethod
    def get_fd(self, name: str, metadata: Dict[str, any] = {}) -> Tuple[Union[str, BinaryIO], str]:
        """
        Create and return a file handle and path

        Parameters
        ----------
        name: str
            Filename used to save data, file path is set by adapter
        metadata: None
            Unused in this Adapter

        Returns
        -------
            file_obj: capy.io.io_adapter.WritableProxyFile
                A thin wrapper of io.IOBase and used in same manner

        """
        pass

    @abstractmethod
    def exists(self, name: str) -> Tuple[bool, str]:
        pass

    @abstractmethod
    def readable(self, name: str) -> bool:
        pass
    
    @abstractmethod
    def read(self, name: str, seekable=False, use_cache_proxy=True) -> IOProxy:
        pass


class WritableProxyFile():
    """
    A class which implements the io.IOBase interface for writing data. It additionally
    persists the data on disk.

    ...

    Attributes
    ----------
    name : str
        Name of the data object
    """

    def __init__(self, name):

        self.name = name
        self.file_obj = tempfile.TemporaryFile("r+b") # delete after uploaded
        self.cnt = 0
        self.closed = False

    def seek(self, offset, whence=io.SEEK_SET):
        """
        Change stream position by offset
        """
        diff = offset - self.cnt
        self.cnt += diff
        self.file_obj.seek(offset, whence)

    def tell(self):
        """
        Return current stream position
        """
        stream_pos = self.file_obj.tell()
        return stream_pos

    def write(self, bytes_obj):
        bytes_written = self.file_obj.write(bytes_obj)
        self.cnt += bytes_written
        return bytes_written

    def truncate(self, size=None):
        return self.file_obj.truncate(size)

    def close(self):
        # logging.debug("WritableProxyFile:Close")
        self._upload()
        r = self.file_obj.close()
        self.closed = True
        return r

    def _upload(self):
        """
        For default FileAdapter just copy file to deisred name/path.
        """
        self.file_obj.flush()
        self.file_obj.seek(0)
        try:
            # logging.debug(f"WritableProxyFile: write data file {self.name}")
            with open(self.name,'w+b') as fobj_name:
                shutil.copyfileobj(self.file_obj, fobj_name)
        except:
            logger.error(f"While copying data {self.name}")
            raise IOError
