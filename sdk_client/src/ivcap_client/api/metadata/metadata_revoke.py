from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.invalid_parameter_value import InvalidParameterValue
from ...models.invalid_scopes_t import InvalidScopesT
from ...models.not_implemented_t import NotImplementedT
from ...types import Response


def _get_kwargs(
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/1/meta/{entity_id}".format(client.base_url, entity_id=entity_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
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
    if response.status_code == 422:
        response_422 = InvalidParameterValue.from_dict(response.json())

        return response_422
    if response.status_code == 501:
        response_501 = NotImplementedT.from_dict(response.json())

        return response_501
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    """revoke metadata

     Retract a previously created statement.

    Args:
        entity_id (str): Record ID to restract Example:
            urn:ivcap:record.53cbb715-4ffd-4158-9e55-5d0ae69605a4.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    """revoke metadata

     Retract a previously created statement.

    Args:
        entity_id (str): Record ID to restract Example:
            urn:ivcap:record.53cbb715-4ffd-4158-9e55-5d0ae69605a4.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]
    """

    return sync_detailed(
        entity_id=entity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    """revoke metadata

     Retract a previously created statement.

    Args:
        entity_id (str): Record ID to restract Example:
            urn:ivcap:record.53cbb715-4ffd-4158-9e55-5d0ae69605a4.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    entity_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    """revoke metadata

     Retract a previously created statement.

    Args:
        entity_id (str): Record ID to restract Example:
            urn:ivcap:record.53cbb715-4ffd-4158-9e55-5d0ae69605a4.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]
    """

    return (
        await asyncio_detailed(
            entity_id=entity_id,
            client=client,
        )
    ).parsed
