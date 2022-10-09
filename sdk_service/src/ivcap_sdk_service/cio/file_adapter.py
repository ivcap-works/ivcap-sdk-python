"""
FileAdapter a thin wrapper around io.IOBase that sets a storage path with
standard filesystem backend
"""
import os
from typing import Tuple, BinaryIO, Dict
import io

from ..logger import sys_logger as logger
from .io_adapter import IOAdapter, WritableProxyFile, ReadProxy

class LocalReadProxy(ReadProxy):
    def __init__(self, name: str):
        self._fname = name

    def open(self, asBinary=True, seekable=False, encoding=None) -> io.IOBase:
        """Return an IO object from which the content this object represents can be read from"""
        mode='r'
        if asBinary: mode = 'rb'
        return io.open(self._fname, mode, encoding=encoding)

    def name(self) -> str:
        return self._fname

    def __repr__(self):
        return f"LocalReadProxy(fname={self._fname})"

class FileAdapter(IOAdapter):
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
    def __init__(self, in_dir: str, out_dir: str) -> None:
        """
        Initialise FileAdapter data paths

        Parameters
        ----------
        order_id: str
            Id of order from API
        in_dir: str
            Path of input data
        out_dir: str
            Path of output data

        Returns
        -------
        None

        """
        super().__init__()
        self.in_dir = in_dir
        self.out_dir = out_dir

    def get_fd(self, name: str, dataPeek: any = None, metadata: Dict[str, any] = {}) -> Tuple[BinaryIO, str]:
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
        file_name = f"{self.out_dir}/{name}"
        logger.debug(f"Returning file handle for '{name} - '{file_name}'")
        file_obj = WritableProxyFile(file_name)
        return (file_obj, f"{file_name}")

    def exists(self, name: str) -> Tuple[bool, str]:
        """
        Check if file exists

        Parameters
        ----------
        name: str
            Filename used to save data, file path is set by adapter

        Returns
        -------
            exists: bool
                File exists as determined by path set in adapter
            file_name: str
                Full path to filename {name}
        """
        file_name = f"{self.out_dir}/{name}"
        file_exists = False
        if os.path.exists(file_name):
            file_exists = True
        return (file_exists,file_name)

    def readable(self, name: str) -> bool:
        file_name = f"{self.in_dir}/{name}"
        return os.path.exists(file_name)

    def read(self, name: str, cache=True) -> ReadProxy:
        file_name = f"{self.in_dir}/{name}"
        if not os.path.exists(file_name):
            raise ValueError(f"Cannot find local file '{file_name}")
        return LocalReadProxy(file_name)

    def __repr__(self):
        return f"FileAdapter(in_dir={self.in_dir}, out_dir={self.out_dir})"


