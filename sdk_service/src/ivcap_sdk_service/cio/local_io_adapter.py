"""
FileAdapter a thin wrapper around io.IOBase that sets a storage path with
standard filesystem backend
"""
import os
from typing import IO, Optional, Tuple, BinaryIO, Dict
import io
import json
from os import access, R_OK
from os.path import isfile
from urllib.parse import urlparse

from .readable_proxy_file import ReadableProxyFile
from .utils import download
from ..utils import json_dump
from ..itypes import MetaDict, Url, SupportedMimeTypes

from ..logger import sys_logger as logger
from .io_adapter import IOAdapter, IOReadable, IOWritable, OnCloseF
from .writable_proxy_file import WritableProxyFile
from .cache import Cache

# class FileProxy(IOProxy):
#     def __init__(self, name: str):
#         self._fname = name
#         self._fhdl = None

#     def open(self, mode: str, **kwargs) -> io.IOBase:
#         """Return an IO object to read or write to depending on 'mode'"""
#         if self._fhdl != None:
#             raise IOError("file '{self._fname}' already opened")
#         self._fhdl = io.open(self._fname, mode=mode, **kwargs)
#         return self._fhdl

#     def close(self):
#         if self._fhdl != None:
#             self._fhdl.close()
#         self._fhdl = None

#     def name(self) -> str:
#         return self._fname

#     def __repr__(self):
#         return f"FileProxy(fname={self._fname}, open={self._fhdl != None})"

class LocalIOAdapter(IOAdapter):
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
    def __init__(self, in_dir: str, out_dir: str, cache: Cache=None) -> None:
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
        self.in_dir = os.path.abspath(in_dir)
        self.out_dir = os.path.abspath(out_dir)
        self.cache = cache

    def read_artifact(self, artifact_id: str, binary_content=True, no_caching=False, seekable=False) -> IOReadable:
        """Return a readable file-like object providing the content of an artifact

        Args:
            artifact_id (str): ID of artifact to read
            binary_content (bool, optional): If true content is expected to be of binary format otherwise text is expected. Defaults to True.
            no_caching (bool, optional): If true, content is not cached nor read from cache. Defaults to False.
            seekable (bool, optional): If true, returned readable should be seekable

        Returns:
            IOReadable: The content of the artifact as a file-like object
        """
        u = urlparse(artifact_id)
        if u.scheme == '' or u.scheme == 'file':
            return self.read_local(u.path, binary_content=binary_content)
        else:
            return self.read_external(artifact_id, binary_content=binary_content, no_caching=no_caching, seekable=seekable)

    def read_external(self, 
        url: Url, 
        binary_content=True, 
        no_caching=False, 
        seekable=False,
        local_file_name=None
    ) -> IOReadable:
        """Return a readable file-like object providing the content of an external data item.

        Args:
            url (Url): URL of external object to read
            binary_content (bool, optional): If true content is expected to be of binary format otherwise text is expected. Defaults to True.
            no_caching (bool, optional): If set, content is not cached nor read from cache. Defaults to False.
            seekable (bool, optional): If true, returned readable should be seekable

        Returns:
            IOReadable: The content of the external data item as a file-like object
        """
        if bool(self.cache) and not no_caching:
            return self.cache.get_and_cache_file(url)

        if bool(local_file_name):
            name = local_file_name
            use_temp_file = False
        else:
            p = urlparse(url).path
            p = p if p != '' else '/index.html'
            p = p if p[0] != '/' else p[1:]
            name = p.replace('/', '__')
            use_temp_file = True
        path = self._to_path(self.in_dir, name)
        ior = ReadableProxyFile(url, path, is_binary=binary_content, writable_also=True, use_temp_file=use_temp_file)
        download(url, ior._file_obj, close_fhdl=False)
        logger.debug("LocalIOAdapter#read_external: Read external content '%s' into '%s'", url, ior.name)
        return ior

    def artifact_readable(self, artifact_id: str) -> bool:
        """Return true if artifact exists and is readable

        Args:
            artifact_id (str): ID of artifact

        Returns:
            bool: True if artifact can be read
        """
        u = urlparse(artifact_id)
        if u.scheme == '' or u.scheme == 'file':
            return self.readable_local(u.path)
        else:
            return True # assume that all external urls are at least conceptually readable
    
    def write_artifact(
        self,
        mime_type: str, 
        name: Optional[str] = None,
        collection_name: Optional[str] = None,
        metadata: Optional[MetaDict] = {}, 
        seekable=False,
        on_close: Optional[OnCloseF] = None
    ) -> IOWritable:
        """Returns a IOWritable to create a new artifact. It needs to be closed
        in order to be persisted. If `on_close` is provided it is called with the 
        artifactID.

        Args:
            mime_type (str): _description_
            name (Optional[str], optional): Optional name. Defaults to None.
            collection_name (Optional[str], optional): Optional collection name. Defaults to None.
            metadata (Optional[MetaDict], optional): Key/value pairs to add as metadata. Defaults to {}.
            seekable (bool, optional): If true, writable should be seekable (needed for NetCDF). Defaults to False.
            on_close (Optional[OnCloseF], optional): Called with assigned artifact ID. Defaults to None.

        Returns:
            IOWritable: A file-like object to write deliver artifact content - needs to be closed
        """
        fname = self._to_path(self.out_dir, name, collection_name)
        if isinstance(mime_type, SupportedMimeTypes):
            mime_type = mime_type.value
        is_binary = not mime_type.startswith('text')

        def _on_close(fd: IO[bytes]):
            logger.info("Written artifact '%s' to '%s'", name, fname)
            if metadata != {}:
                json_dump(metadata, f"{fname}-meta.json")
            if on_close:
                on_close(f"file://{fname}")

        return WritableProxyFile(fname, _on_close, is_binary, use_temp_file=False)

    # def get_fd(self, name: str, dataPeek: any = None, metadata: Dict[str, any] = {}) -> Tuple[BinaryIO, str]:
    #     """
    #     Create and return a file handle and path

    #     Parameters
    #     ----------
    #     name: str
    #         Filename used to save data, file path is set by adapter
    #     metadata: None
    #         Unused in this Adapter

    #     Returns
    #     -------
    #         file_obj: capy.io.io_adapter.WritableProxyFile
    #             A thin wrapper of io.IOBase and used in same manner

    #     """
    #     file_name = f"{self.out_dir}/{name}"
    #     logger.debug(f"Returning file handle for '{name}' - '{file_name}'")
    #     file_obj = WritableProxyFile(file_name)
    #     return (file_obj, f"{file_name}")

    def readable_local(self, name: str, collection_name: str = None) -> bool:
        """Return true if file exists and is readable. If 'name' starts with a '/'
        it is assumed to be an absolute path. If not, it's assumed to be local to self._in_dir

        Args:
            name (str): Name of file or path to it when it starts with '/'
            collection_name (str, optional): Optional collection name which would create local directory. Defaults to None.

        Returns:
            bool: True if file is readable
        """
        file_name = self._to_path(self.in_dir, name, collection_name)
        return isfile(file_name) and access(file_name, R_OK)

        # file_exists = False
        # if os.path.exists(file_name):
        #     file_exists = True
        # return (file_exists,file_name)

    def read_local(self, name: str, collection_name: str = None, binary_content=True) -> IOReadable:
        """Return a readable file-like object providing the content of an external data item.

        Args:
            name (str): Name of file or path to it when it starts with '/'
            collection_name (str, optional): Optional collection name which would create local directory. Defaults to None.
            binary_content (bool, optional): If true content is expected to be of binary format otherwise text is expected. Defaults to True.

        Returns:
            IOReadable: The content of the local file as a file-like object
        """
        path = self._to_path(self.in_dir, name, collection_name)
        return ReadableProxyFile(name, path, is_binary=binary_content, use_temp_file=False)

    # def readable(self, name: str, collection_name: str = None) -> bool:
    #     file_name = self._to_path(self.in_dir, name, collection_name)
    #     return os.path.exists(file_name)

    def _to_path(self, prefix: str, name: str, collection_name: str = None) -> str:
        if name.startswith('/'):
            return name
        elif name.startswith('file:'):
            return name[len('file://'):]
        else:
            if collection_name:
                return os.path.join(prefix, collection_name, name)
            else:
                return os.path.join(prefix, name)

    # def read(self, name: str, seekable=False, use_cache_proxy=True) -> IOProxy:
    #     file_name = self._to_path(name)
    #     if not os.path.exists(file_name):
    #         raise ValueError(f"Cannot find local file '{file_name}")
    #     return FileProxy(file_name)

    def __repr__(self):
        return f"<LocalIOAdapter in_dir={self.in_dir} out_dir={self.out_dir}>"

