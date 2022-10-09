from abc import ABC, abstractmethod
from typing import Tuple, Union, BinaryIO, Dict
import tempfile
import io
import shutil
from ..logger import logger

class ReadProxy(ABC):
    """Represents a file-like object to read from"""

    @abstractmethod
    def open(self, asBinary=True, seekable=False, encoding=None) -> io.IOBase:
        """Return an IO object from which the content this object represents can be read from"""

    @abstractmethod
    def name(self) -> str:
        """Returns name of underlying object"""
        pass

        
class IOAdapter(ABC):

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
    def read(self, name: str, cache=True) -> ReadProxy:
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
