from builtins import BaseException
import pathlib
from typing import IO, AnyStr, Callable, List, Tuple, Union, BinaryIO, Dict
import tempfile
import io
import shutil
from ..logger import sys_logger as logger

from .io_adapter import IOReadable

class ReadableProxyFile(IOReadable):

    def __init__(self, 
        name: str,
        path: str,
        on_close: Callable[[IO[bytes]], None]=None, 
        is_binary=True, 
        use_temp_file=True, 
        encoding=None,
        writable_also=False
    ):
        if writable_also:
            # needed for temporary files which are first written
            self._mode = "w+b" if is_binary else "w+"
        else:
            self._mode = "rb" if is_binary else "r"
        if use_temp_file:
            self._file_obj = tempfile.NamedTemporaryFile(self._mode, encoding=encoding) # delete after uploaded
            self._path = self._file_obj.name
        else:
            self._path = path
            self._file_obj = io.open(path, mode=self._mode, encoding=encoding)
        self._name = name
        self._on_close = on_close
        self._closed = False

    @property
    def closed(self) -> bool:
        return self._closed

    @property
    def mode(self) -> str:
        return self._mode

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        return self._path

    def writable(self) -> bool:
        return False

    def readable(self) -> bool:
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        """
        Change stream position by offset
        """
        return self._file_obj.seek(offset, whence)

    def seekable(self) -> bool:
        return True

    def tell(self) -> int:
        """
        Return current stream position
        """
        return self._file_obj.tell()

    def read(self, n: int = -1) -> AnyStr:
        return self._file_obj.read(n)

    def readline(self, limit: int = -1) -> AnyStr:
        return self._file_obj.readline(limit)

    def readlines(self, hint: int = -1) -> List[AnyStr]:
        return self._file_obj.readlines(hint)

    def close(self):
        self._closed = True
        
        try:
            if self._on_close:
                self._on_close(self._file_obj)
        except BaseException as err:
            logger.warn("ReadableProxyFile#close: on_close '%s' failed with '%s'", self._on_close, err)
        finally:
            self._file_obj.close()

    def __repr__(self):
        return f"<ReadableProxyFile name={self._name} closed={self._closed} mode={self._mode} fp={self._file_obj}>"

    def to_json(self):
        return self._name