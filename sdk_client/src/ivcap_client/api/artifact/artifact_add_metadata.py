from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.invalid_scopes_t import InvalidScopesT
from ...models.not_implemented_t import NotImplementedT
from ...models.resource_not_found_t import ResourceNotFoundT
from ...types import File, Response


def _get_kwargs(
    id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    json_body: File,
) -> Dict[str, Any]:
    url = "{}/1/artifacts/{id}/.metadata/{schema}".format(client.base_url, id=id, schema=schema)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_tuple()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = InvalidScopesT.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ResourceNotFoundT.from_dict(response.json())

        return response_404
    if response.status_code == 501:
        response_501 = NotImplementedT.from_dict(response.json())

        return response_501
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    json_body: File,
) -> Response[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    """addMetadata artifact

     Add metadata of a partiular schema to artifacts.

    Args:
        id (str): Artifact ID Example: type:scope:name.
        schema (str): Schema of metadata. This will replace any existing metadata with this
            schema. Example: urn:image:gopro.
        json_body (File): Metadata of a specific schema. Example: Eaque explicabo..

    Returns:
        Response[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]
    """

    kwargs = _get_kwargs(
        id=id,
        schema=schema,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    json_body: File,
) -> Optional[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    """addMetadata artifact

     Add metadata of a partiular schema to artifacts.

    Args:
        id (str): Artifact ID Example: type:scope:name.
        schema (str): Schema of metadata. This will replace any existing metadata with this
            schema. Example: urn:image:gopro.
        json_body (File): Metadata of a specific schema. Example: Eaque explicabo..

    Returns:
        Response[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]
    """

    return sync_detailed(
        id=id,
        schema=schema,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    json_body: File,
) -> Response[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    """addMetadata artifact

     Add metadata of a partiular schema to artifacts.

    Args:
        id (str): Artifact ID Example: type:scope:name.
        schema (str): Schema of metadata. This will replace any existing metadata with this
            schema. Example: urn:image:gopro.
        json_body (File): Metadata of a specific schema. Example: Eaque explicabo..

    Returns:
        Response[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]
    """

    kwargs = _get_kwargs(
        id=id,
        schema=schema,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    json_body: File,
) -> Optional[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    """addMetadata artifact

     Add metadata of a partiular schema to artifacts.

    Args:
        id (str): Artifact ID Example: type:scope:name.
        schema (str): Schema of metadata. This will replace any existing metadata with this
            schema. Example: urn:image:gopro.
        json_body (File): Metadata of a specific schema. Example: Eaque explicabo..

    Returns:
        Response[Union[Any, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]
    """

    return (
        await asyncio_detailed(
            id=id,
            schema=schema,
            client=client,
            json_body=json_body,
        )
    ).parsed
