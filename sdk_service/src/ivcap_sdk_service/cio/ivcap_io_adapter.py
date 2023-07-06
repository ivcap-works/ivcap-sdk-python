#
# Copyright (c) 2023 Commonwealth Scientific and Industrial Research Organisation (CSIRO). All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file. See the AUTHORS file for names of contributors.
#
"""
Implementation of the IOAdapter class for use inside the IVCAP platform
"""
import base64
import os
import sys
from typing import IO, Callable, Optional, Sequence, Tuple, BinaryIO, Dict, Union
import io
import json
from os import access, R_OK
from os.path import isfile
import requests
from urllib.parse import urlparse
import collections.abc

from .readable_proxy_file import ReadableProxyFile
from .utils import download
from ..utils import json_dump
from ..itypes import MetaDict, Url, SupportedMimeTypes

from ..logger import sys_logger as logger
from .io_adapter import Collection, IOAdapter, IOReadable, IOWritable, OnCloseF
from .writable_proxy_file import WritableProxyFile
from .cache import Cache

class IvcapIOAdapter(IOAdapter):
    """
    An adapter for operating inside an IVCAP container.
    """
    def __init__(self, 
        storage_url: Url, 
        in_dir: str, 
        out_dir: str, 
        order_id:str, 
        cachable_url: Callable[[str], str],
        cache: Cache=None,
    ) -> None:
        super().__init__()
        self.in_dir = os.path.abspath(in_dir)
        self.out_dir = os.path.abspath(out_dir)
        self.storage_url = storage_url
        self.cachable_url = cachable_url
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

        # u = urlparse(artifact_id)
        # curl = self.cachable_url(artifact_id)
        # if u.scheme == '' or u.scheme == 'file':
        #     return self.read_local(u.path, binary_content=binary_content)
        # else:
        #     
        return self.read_external(artifact_id, binary_content=binary_content, no_caching=True, seekable=seekable)

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
        if url.startswith(self.storage_url):
            curl = url
        else:
            curl = self.cachable_url(url)
        ior = ReadableProxyFile(name, path, is_binary=binary_content, writable_also=True, use_temp_file=use_temp_file)
        download(curl, ior._file_obj, close_fhdl=False)
        logger.debug("LocalIOAdapter#read_external: Read external content '%s' into '%s'", curl, ior.path)
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
        metadata: Optional[Union[MetaDict, Sequence[MetaDict]]] = None, 
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
        if isinstance(mime_type, SupportedMimeTypes):
            mime_type = mime_type.value
        is_binary = not mime_type.startswith('text')

        def _on_close(fd: IO[bytes], fname):
            url = self._upload_artifact(fd, mime_type, name, collection_name, metadata)
            if on_close:
                on_close(url)

        return WritableProxyFile("", _on_close, is_binary, use_temp_file=True, readable_also=True)

    def _upload_artifact(
        self, 
        fd: IO[bytes], 
        mime_type: str, 
        name: Optional[str],
        collection_name: Optional[str],
        metadata: Optional[Union[MetaDict, Sequence[MetaDict]]],
    ) -> Url:
        logger.info("Upload artifact '%s'", name)
        fd.flush()
        fd.seek(0)

        if metadata:
            if not isinstance(metadata, collections.Sequence):
                metadata = [metadata]
        else:
            metadata = []
        metadataUploaded = False

        # dataType = str(type(self.dataPeek))
        # ct = type2mime.get(dataType, "unknown")
        headers = {
            "Content-Type": mime_type,
        }
        if name:
            headers["X-Name"] = name

        if len(metadata) == 1 and len(metadata[0].keys()) <= 3:
            # Immediately upload simple metadata
            metadataUploaded = True
            headers['Upload-Metadata'] = ','. join(map(lambda e: f"{e[0]} {encode64(str(e[1]))}", metadata[0].items()))
        try:
            logger.debug("Post artifact data='%s', headers:'%s'", fd, headers)
            r = requests.post(self.storage_url, data=fd, headers=headers)
        except:
            print(">>>>", sys.exc_info())
            logger.fatal(f"while posting result data {self.storage_url} - {sys.exc_info()[0]}")
            sys.exit(-1)
        if r.status_code >= 300:
            logger.fatal(f"error response {r.status_code} while posting result data {self.storage_url}")
            sys.exit(-1)

        url = r.headers.get('Location')
        artifactID = r.headers.get('X-Artifact-Id')
        size = int(r.headers.get('Content-Length', -1))
        logger.info(f"IvcapIOAdapter: created artifact '{artifactID}' of size '{size}' via '{self.storage_url}'")

        if not metadataUploaded and len(metadata) > 0:
            self._upload_metadata(metadata, artifactID, url)
        return url

    def _upload_metadata(
        self, 
        metadata: Sequence[MetaDict],
        artifactID: str,
        url: str,
    ) -> None:
        for md in metadata:
            headers = {
                "X-Meta-Data-For-Url": url,
                "X-Meta-Data-For-Artifact": artifactID,
                "X-Meta-Data-Schema": md.get('$schema', '???'),
                "Content-Type": "application/json",
            }
            # u = urlparse(self.url)
            # p = f"{u.path.replace('.', '-')}-meta.json"
            # murl = u._replace(path=p).geturl()
            try:
                logger.debug("Post artifact metadata data='%s', headers:'%s'", md, headers)
                payload = json_dump(md)
                r = requests.post(self.storage_url, data=payload, headers=headers)
            except:
                logger.fatal(f"while posting metadata {self.storage_url} - {sys.exc_info()}")
                sys.exit(-1)
            if r.status_code >= 300:
                logger.fatal(f"error response {r.status_code} while posting metadata {self.storage_url}")
                sys.exit(-1)


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

    def get_collection(self, collection_urn: str) -> Collection:
        return IvcapCollection(collection_urn)

    # def read(self, name: str, seekable=False, use_cache_proxy=True) -> IOProxy:
    #     file_name = self._to_path(name)
    #     if not os.path.exists(file_name):
    #         raise ValueError(f"Cannot find local file '{file_name}")
    #     return FileProxy(file_name)

    def __repr__(self):
        return f"<IvcapIOAdapter in_dir={self.in_dir} out_dir={self.out_dir}>"


class IvcapCollection(Collection):
    def __init__(self, collection_urn: str) -> None:
        super().__init__()
        self._collection_urn = collection_urn

def encode64(s: str) -> str:
    sb = s.encode('ascii')
    ba = base64.b64encode(sb)
    return ba.decode('ascii')
