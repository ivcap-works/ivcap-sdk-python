#
# Copyright (c) 2023 Commonwealth Scientific and Industrial Research Organisation (CSIRO). All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file. See the AUTHORS file for names of contributors.
#
from builtins import BaseException
from typing import IO, AnyStr, Callable, List, Optional
import tempfile
import io

from ivcap_sdk_service.cio.utils import download
from ..logger import sys_logger as logger

from .io_adapter import IOReadable

class ReadableProxyFile(IOReadable):

    def __init__(self, 
        name: str,
        path: Optional[str],
        download_url: Optional[str],
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

        self._name = name
        self._path = path
        self._is_binary = is_binary
        self._download_url = download_url
        self._use_temp_file = use_temp_file
        self._encoding = encoding
        self._on_close = on_close
        self._writable_also = writable_also
        self._offset = 0
        self._file_obj = None
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

    def as_local_file(self) -> str:
        self._get_file_obj()
        return self._path

    def writable(self) -> bool:
        return self._writable_also

    def readable(self) -> bool:
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        """
        Change stream position by offset
        """
        # if whence == io.SEEK_SET:
        #     self._offset = offset
        # elif whence == io.SEEK_CUR:
        #     self._offset += offset
        # else:
        #     raise OSError(-1, "cannot seek from end")
        self._get_file_obj().seek(offset, whence)

    def seekable(self) -> bool:
        return True

    def tell(self) -> int:
        """
        Return current stream position
        """
        return self._get_file_obj().tell()

    def read(self, n: int = -1) -> AnyStr:
        return self._get_file_obj().read(n)

    def readline(self, limit: int = -1) -> AnyStr:
        return self._get_file_obj().readline(limit)

    def readlines(self, hint: int = -1) -> List[AnyStr]:
        return self._get_file_obj().readlines(hint)

    def close(self):
        self._closed = True
        f = self._get_file_obj()
        try:
            if self._on_close:
                self._on_close(f)
        except BaseException as err:
            logger.warn("ReadableProxyFile#close: on_close '%s' failed with '%s'", self._on_close, err)
        finally:
            f.close()

    def _get_file_obj(self):
        if self._file_obj == None:
            self._open_file_obj()
        return self._file_obj
    
    def _open_file_obj(self):
        """Open and ensure that the local file object is properly "filled".

        If the content is from an external source, ensure that it is fully
        downloaded into `_file_obj`.
        """

        if self._download_url:
            mode = "w+b" if self._is_binary else "w+"
            self._file_obj = tempfile.NamedTemporaryFile(mode, encoding=self._encoding)
            self._path = self._file_obj.name
            try:
                download(self._download_url, self._file_obj, close_fhdl=False)
            except BaseException as ex:
                logger.error("ReadableProxyFile#_open_file_obj: While downloading - %s", ex.__repr__())
                raise ex
            
            logger.debug("ReadableProxyFile#_open_file_obj: Read external content '%s' into '%s'", self._download_url, self._path)

        elif self._path:
            self._file_obj = io.open(self._path, mode=self._mode, encoding=self._encoding)

    def __repr__(self):
        return f"<ReadableProxyFile name={self._name} closed={self._closed} mode={self._mode}>"

    def to_json(self):
        return self._name
