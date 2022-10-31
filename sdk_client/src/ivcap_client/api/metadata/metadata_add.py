from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.add_meta_rt import AddMetaRT
from ...models.invalid_parameter_value import InvalidParameterValue
from ...models.invalid_scopes_t import InvalidScopesT
from ...models.not_implemented_t import NotImplementedT
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity_id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/1/meta/{entity_id}/{schema}".format(client.base_url, entity_id=entity_id, schema=schema)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(content_type, Unset):
        headers["Content-Type"] = content_type

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    if response.status_code == 200:
        response_200 = AddMetaRT.from_dict(response.json())

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
    if response.status_code == 422:
        response_422 = InvalidParameterValue.from_dict(response.json())

        return response_422
    if response.status_code == 501:
        response_501 = NotImplementedT.from_dict(response.json())

        return response_501
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    entity_id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Response[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    """add metadata

     Attach new metadata to an entity.

    Args:
        entity_id (str): Entity to which attach metadata Example:
            http://gerlach.org/jarrell.schinner.
        schema (str): Schema of metadata Example: http://bashirian.biz/zachary_kautzer.
        content_type (Union[Unset, str]): Content-Type header, MUST be of application/json.
            Example: application/json.

    Returns:
        Response[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        schema=schema,
        client=client,
        content_type=content_type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    entity_id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Optional[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    """add metadata

     Attach new metadata to an entity.

    Args:
        entity_id (str): Entity to which attach metadata Example:
            http://gerlach.org/jarrell.schinner.
        schema (str): Schema of metadata Example: http://bashirian.biz/zachary_kautzer.
        content_type (Union[Unset, str]): Content-Type header, MUST be of application/json.
            Example: application/json.

    Returns:
        Response[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]
    """

    return sync_detailed(
        entity_id=entity_id,
        schema=schema,
        client=client,
        content_type=content_type,
    ).parsed


async def asyncio_detailed(
    entity_id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Response[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    """add metadata

     Attach new metadata to an entity.

    Args:
        entity_id (str): Entity to which attach metadata Example:
            http://gerlach.org/jarrell.schinner.
        schema (str): Schema of metadata Example: http://bashirian.biz/zachary_kautzer.
        content_type (Union[Unset, str]): Content-Type header, MUST be of application/json.
            Example: application/json.

    Returns:
        Response[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        schema=schema,
        client=client,
        content_type=content_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    entity_id: str,
    schema: str,
    *,
    client: AuthenticatedClient,
    content_type: Union[Unset, str] = UNSET,
) -> Optional[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]:
    """add metadata

     Attach new metadata to an entity.

    Args:
        entity_id (str): Entity to which attach metadata Example:
            http://gerlach.org/jarrell.schinner.
        schema (str): Schema of metadata Example: http://bashirian.biz/zachary_kautzer.
        content_type (Union[Unset, str]): Content-Type header, MUST be of application/json.
            Example: application/json.

    Returns:
        Response[Union[AddMetaRT, Any, InvalidParameterValue, InvalidScopesT, NotImplementedT]]
    """

    return (
        await asyncio_detailed(
            entity_id=entity_id,
            schema=schema,
            client=client,
            content_type=content_type,
        )
    ).parsed
