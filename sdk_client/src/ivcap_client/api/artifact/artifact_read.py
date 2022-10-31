from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.artifact_status_rt import ArtifactStatusRT
from ...models.invalid_scopes_t import InvalidScopesT
from ...models.not_implemented_t import NotImplementedT
from ...models.resource_not_found_t import ResourceNotFoundT
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/1/artifacts/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    if response.status_code == 200:
        response_200 = ArtifactStatusRT.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    """read artifact

     Show artifacts by ID

    Args:
        id (str): ID of artifacts to show Example: type:scope:name.

    Returns:
        Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    """read artifact

     Show artifacts by ID

    Args:
        id (str): ID of artifacts to show Example: type:scope:name.

    Returns:
        Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    """read artifact

     Show artifacts by ID

    Args:
        id (str): ID of artifacts to show Example: type:scope:name.

    Returns:
        Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]:
    """read artifact

     Show artifacts by ID

    Args:
        id (str): ID of artifacts to show Example: type:scope:name.

    Returns:
        Response[Union[Any, ArtifactStatusRT, InvalidScopesT, NotImplementedT, ResourceNotFoundT]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
