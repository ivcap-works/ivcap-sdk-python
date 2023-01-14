from builtins import BaseException
from typing import IO, AnyStr, Callable, List, Tuple, Union, BinaryIO, Dict
import tempfile
import io
import shutil
from ..logger import sys_logger as logger

from .io_adapter import IOWritable

class WritableProxyFile(IOWritable):
    """
    A class which implements the IOWritable interface for writing data. It additionally
    persists the data on disk.

    ...

    Args:
        name (str): _description_
        on_close (Callable[[IO[bytes], None]]): _description_. Defaults to None.
        is_binary (bool, optional): _description_. Defaults to True.
        use_temp_file (bool, optional): _description_. Defaults to True.
        encoding (_type_, optional): _description_. Defaults to None.
    """

    def __init__(self, name: str, on_close: Callable[[IO[bytes]], None]=None, is_binary=True, use_temp_file=True, encoding=None):
        
        self._mode = "wb" if is_binary else "w"
        if use_temp_file:
            self._file_obj = tempfile.NamedTemporaryFile(self._mode, encoding=encoding) # delete after uploaded
            self._name = self._file_obj.name
        else:
            self._file_obj = io.open(name, mode=self._mode, encoding=encoding)
            self._name = name
        self.cnt = 0
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

    def seek(self, offset, whence=io.SEEK_SET):
        """
        Change stream position by offset
        """
        diff = offset - self.cnt
        self.cnt += diff
        self._file_obj.seek(offset, whence)

    def seekable(self) -> bool:
        return True

    def tell(self) -> int:
        """
        Return current stream position
        """
        stream_pos = self._file_obj.tell()
        return stream_pos

    def write(self, bytes_obj: AnyStr) -> int:
        bytes_written = self._file_obj.write(bytes_obj)
        self.cnt += bytes_written
        return bytes_written

    def writelines(self, lines: List[AnyStr]) -> None:
        self._file_obj.writelines(lines)

    def writable(self) -> bool:
        return True

    def truncate(self, size: int = None) -> int:
        self.cnt = self._file_obj.truncate(size)
        return self.cnt

    def readable(self) -> bool:
        return False

    def flush(self) -> None:
        self._file_obj.flush()

    def close(self):
        # logging.debug("WritableProxyFile:Close")
        #self._upload()
        self._closed = True
        self._file_obj.flush()
        #self.file_obj.seek(0)
        try:
            if self._on_close:
                self._on_close(self._file_obj)
        except BaseException as err:
            logger.warn("WritableProxyFile#close: on_close '%s' failed with '%s'", self._on_close, err)
        finally:
            self._file_obj.close()

    # def _upload(self):
    #     """
    #     For default FileAdapter just copy file to deisred name/path.
    #     """
    #     self._file_obj.flush()
    #     self._file_obj.seek(0)
    #     try:
    #         # logging.debug(f"WritableProxyFile: write data file {self.name}")
    #         with open(self.name,'w+b') as fobj_name:
    #             shutil.copyfileobj(self._file_obj, fobj_name)
    #     except:
    #         logger.error(f"While copying data {self.name}")
    #         raise IOError

    def __repr__(self):
        return f"<WritableProxyFile name={self._name} closed={self._closed} mode={self._mode} fp={self._file_obj}>"
