from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.artifact_status_rt import ArtifactStatusRT
from ...models.invalid_scopes_t import InvalidScopesT
from ...models.not_implemented_t import NotImplementedT
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
    content_encoding: Union[Unset, str] = UNSET,
    content_length: Union[Unset, int] = UNSET,
    x_name: Union[Unset, str] = UNSET,
    x_collection: Union[Unset, str] = UNSET,
    upload_metadata: Union[Unset, str] = UNSET,
    x_content_type: Union[Unset, str] = UNSET,
    upload_length: Union[Unset, int] = UNSET,
    tus_resumable: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/1/artifacts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(content_type, Unset):
        headers["Content-Type"] = content_type

    if not isinstance(content_encoding, Unset):
        headers["Content-Encoding"] = content_encoding

    if not isinstance(content_length, Unset):
        headers["Content-Length"] = str(content_length)

    if not isinstance(x_name, Unset):
        headers["X-Name"] = x_name

    if not isinstance(x_collection, Unset):
        headers["X-Collection"] = x_collection

    if not isinstance(upload_metadata, Unset):
        headers["Upload-Metadata"] = upload_metadata

    if not isinstance(x_content_type, Unset):
        headers["X-Content-Type"] = x_content_type

    if not isinstance(upload_length, Unset):
        headers["Upload-Length"] = str(upload_length)

    if not isinstance(tus_resumable, Unset):
        headers["Tus-Resumable"] = tus_resumable

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]:
    if response.status_code == 201:
        response_201 = ArtifactStatusRT.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = InvalidScopesT.from_dict(response.json())

        return response_403
    if response.status_code == 501:
        response_501 = NotImplementedT.from_dict(response.json())

        return response_501
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
    content_encoding: Union[Unset, str] = UNSET,
    content_length: Union[Unset, int] = UNSET,
    x_name: Union[Unset, str] = UNSET,
    x_collection: Union[Unset, str] = UNSET,
    upload_metadata: Union[Unset, str] = UNSET,
    x_content_type: Union[Unset, str] = UNSET,
    upload_length: Union[Unset, int] = UNSET,
    tus_resumable: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]:
    """upload artifact

     Upload content and create a artifacts.

    Args:
        content_type (Union[Unset, str]): Content-Type header, MUST define type of uploaded
            content. Example: application/x-netcdf4.
        content_encoding (Union[Unset, str]): Content-Encoding header, MAY define encoding of
            content. Example: gzip.
        content_length (Union[Unset, int]): Content-Length header, MAY define size of expected
            upload. Example: 2376.
        x_name (Union[Unset, str]): X-Name header, MAY define a more human friendly name. Reusing
            a name will NOT override an existing artifact with the same name Example: field-trip-
            jun-22.
        x_collection (Union[Unset, str]): X-Collection header, MAY define an collection name as a
            simple way of grouping artifacts Example: field-trip-jun-22.
        upload_metadata (Union[Unset, str]): The Upload-Metadata request and response header MUST
            consist of one or more
                                        comma-separated key-value pairs. The key and value MUST be separated by a space.
                                        The key MUST NOT contain spaces and commas and MUST NOT be empty. The key SHOULD be
            ASCII
                                        encoded and the value MUST be Base64 encoded. All keys MUST be unique. The value MAY
            be empty.
                                        In these cases, the space, which would normally separate the key and the value, MAY be
            left out.
                                        See https://tus.io/protocols/resumable-upload.html#upload-metadata Example: filename
            d29ybGRfZG9taW5hdGlvbl9wbGFuLnBkZg==,is_confidential.
        x_content_type (Union[Unset, str]): X-Content-Type header, used for initial, empty content
            creation requests. Example: application/x-netcdf4.
        upload_length (Union[Unset, int]): Upload-Length header, sets the expected content size
            part of the TUS protocol. Example: 2376.
        tus_resumable (Union[Unset, str]): Tus-Resumable header, specifies TUS protocol version.
            Example: 1.0.0.

    Returns:
        Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]
    """

    kwargs = _get_kwargs(
        client=client,
        content_type=content_type,
        content_encoding=content_encoding,
        content_length=content_length,
        x_name=x_name,
        x_collection=x_collection,
        upload_metadata=upload_metadata,
        x_content_type=x_content_type,
        upload_length=upload_length,
        tus_resumable=tus_resumable,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
    content_encoding: Union[Unset, str] = UNSET,
    content_length: Union[Unset, int] = UNSET,
    x_name: Union[Unset, str] = UNSET,
    x_collection: Union[Unset, str] = UNSET,
    upload_metadata: Union[Unset, str] = UNSET,
    x_content_type: Union[Unset, str] = UNSET,
    upload_length: Union[Unset, int] = UNSET,
    tus_resumable: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]:
    """upload artifact

     Upload content and create a artifacts.

    Args:
        content_type (Union[Unset, str]): Content-Type header, MUST define type of uploaded
            content. Example: application/x-netcdf4.
        content_encoding (Union[Unset, str]): Content-Encoding header, MAY define encoding of
            content. Example: gzip.
        content_length (Union[Unset, int]): Content-Length header, MAY define size of expected
            upload. Example: 2376.
        x_name (Union[Unset, str]): X-Name header, MAY define a more human friendly name. Reusing
            a name will NOT override an existing artifact with the same name Example: field-trip-
            jun-22.
        x_collection (Union[Unset, str]): X-Collection header, MAY define an collection name as a
            simple way of grouping artifacts Example: field-trip-jun-22.
        upload_metadata (Union[Unset, str]): The Upload-Metadata request and response header MUST
            consist of one or more
                                        comma-separated key-value pairs. The key and value MUST be separated by a space.
                                        The key MUST NOT contain spaces and commas and MUST NOT be empty. The key SHOULD be
            ASCII
                                        encoded and the value MUST be Base64 encoded. All keys MUST be unique. The value MAY
            be empty.
                                        In these cases, the space, which would normally separate the key and the value, MAY be
            left out.
                                        See https://tus.io/protocols/resumable-upload.html#upload-metadata Example: filename
            d29ybGRfZG9taW5hdGlvbl9wbGFuLnBkZg==,is_confidential.
        x_content_type (Union[Unset, str]): X-Content-Type header, used for initial, empty content
            creation requests. Example: application/x-netcdf4.
        upload_length (Union[Unset, int]): Upload-Length header, sets the expected content size
            part of the TUS protocol. Example: 2376.
        tus_resumable (Union[Unset, str]): Tus-Resumable header, specifies TUS protocol version.
            Example: 1.0.0.

    Returns:
        Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]
    """

    return sync_detailed(
        client=client,
        content_type=content_type,
        content_encoding=content_encoding,
        content_length=content_length,
        x_name=x_name,
        x_collection=x_collection,
        upload_metadata=upload_metadata,
        x_content_type=x_content_type,
        upload_length=upload_length,
        tus_resumable=tus_resumable,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
    content_encoding: Union[Unset, str] = UNSET,
    content_length: Union[Unset, int] = UNSET,
    x_name: Union[Unset, str] = UNSET,
    x_collection: Union[Unset, str] = UNSET,
    upload_metadata: Union[Unset, str] = UNSET,
    x_content_type: Union[Unset, str] = UNSET,
    upload_length: Union[Unset, int] = UNSET,
    tus_resumable: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]:
    """upload artifact

     Upload content and create a artifacts.

    Args:
        content_type (Union[Unset, str]): Content-Type header, MUST define type of uploaded
            content. Example: application/x-netcdf4.
        content_encoding (Union[Unset, str]): Content-Encoding header, MAY define encoding of
            content. Example: gzip.
        content_length (Union[Unset, int]): Content-Length header, MAY define size of expected
            upload. Example: 2376.
        x_name (Union[Unset, str]): X-Name header, MAY define a more human friendly name. Reusing
            a name will NOT override an existing artifact with the same name Example: field-trip-
            jun-22.
        x_collection (Union[Unset, str]): X-Collection header, MAY define an collection name as a
            simple way of grouping artifacts Example: field-trip-jun-22.
        upload_metadata (Union[Unset, str]): The Upload-Metadata request and response header MUST
            consist of one or more
                                        comma-separated key-value pairs. The key and value MUST be separated by a space.
                                        The key MUST NOT contain spaces and commas and MUST NOT be empty. The key SHOULD be
            ASCII
                                        encoded and the value MUST be Base64 encoded. All keys MUST be unique. The value MAY
            be empty.
                                        In these cases, the space, which would normally separate the key and the value, MAY be
            left out.
                                        See https://tus.io/protocols/resumable-upload.html#upload-metadata Example: filename
            d29ybGRfZG9taW5hdGlvbl9wbGFuLnBkZg==,is_confidential.
        x_content_type (Union[Unset, str]): X-Content-Type header, used for initial, empty content
            creation requests. Example: application/x-netcdf4.
        upload_length (Union[Unset, int]): Upload-Length header, sets the expected content size
            part of the TUS protocol. Example: 2376.
        tus_resumable (Union[Unset, str]): Tus-Resumable header, specifies TUS protocol version.
            Example: 1.0.0.

    Returns:
        Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]
    """

    kwargs = _get_kwargs(
        client=client,
        content_type=content_type,
        content_encoding=content_encoding,
        content_length=content_length,
        x_name=x_name,
        x_collection=x_collection,
        upload_metadata=upload_metadata,
        x_content_type=x_content_type,
        upload_length=upload_length,
        tus_resumable=tus_resumable,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
    content_encoding: Union[Unset, str] = UNSET,
    content_length: Union[Unset, int] = UNSET,
    x_name: Union[Unset, str] = UNSET,
    x_collection: Union[Unset, str] = UNSET,
    upload_metadata: Union[Unset, str] = UNSET,
    x_content_type: Union[Unset, str] = UNSET,
    upload_length: Union[Unset, int] = UNSET,
    tus_resumable: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]:
    """upload artifact

     Upload content and create a artifacts.

    Args:
        content_type (Union[Unset, str]): Content-Type header, MUST define type of uploaded
            content. Example: application/x-netcdf4.
        content_encoding (Union[Unset, str]): Content-Encoding header, MAY define encoding of
            content. Example: gzip.
        content_length (Union[Unset, int]): Content-Length header, MAY define size of expected
            upload. Example: 2376.
        x_name (Union[Unset, str]): X-Name header, MAY define a more human friendly name. Reusing
            a name will NOT override an existing artifact with the same name Example: field-trip-
            jun-22.
        x_collection (Union[Unset, str]): X-Collection header, MAY define an collection name as a
            simple way of grouping artifacts Example: field-trip-jun-22.
        upload_metadata (Union[Unset, str]): The Upload-Metadata request and response header MUST
            consist of one or more
                                        comma-separated key-value pairs. The key and value MUST be separated by a space.
                                        The key MUST NOT contain spaces and commas and MUST NOT be empty. The key SHOULD be
            ASCII
                                        encoded and the value MUST be Base64 encoded. All keys MUST be unique. The value MAY
            be empty.
                                        In these cases, the space, which would normally separate the key and the value, MAY be
            left out.
                                        See https://tus.io/protocols/resumable-upload.html#upload-metadata Example: filename
            d29ybGRfZG9taW5hdGlvbl9wbGFuLnBkZg==,is_confidential.
        x_content_type (Union[Unset, str]): X-Content-Type header, used for initial, empty content
            creation requests. Example: application/x-netcdf4.
        upload_length (Union[Unset, int]): Upload-Length header, sets the expected content size
            part of the TUS protocol. Example: 2376.
        tus_resumable (Union[Unset, str]): Tus-Resumable header, specifies TUS protocol version.
            Example: 1.0.0.

    Returns:
        Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT]]
    """

    return (
        await asyncio_detailed(
            client=client,
            content_type=content_type,
            content_encoding=content_encoding,
            content_length=content_length,
            x_name=x_name,
            x_collection=x_collection,
            upload_metadata=upload_metadata,
            x_content_type=x_content_type,
            upload_length=upload_length,
            tus_resumable=tus_resumable,
        )
    ).parsed
