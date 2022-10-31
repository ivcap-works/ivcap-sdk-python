import datetime
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.invalid_parameter_value import InvalidParameterValue
from ...models.invalid_scopes_t import InvalidScopesT
from ...models.not_implemented_t import NotImplementedT
from ...models.read_meta_rt import ReadMetaRT
from ...types import UNSET, Response, Unset


def _get_kwargs(
    entity_id: str,
    *,
    client: AuthenticatedClient,
    schema_filter: Union[Unset, None, str] = UNSET,
    at_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    url = "{}/1/meta/{entity_id}".format(client.base_url, entity_id=entity_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$schema-filter"] = schema_filter

    json_at_time: Union[Unset, None, str] = UNSET
    if not isinstance(at_time, Unset):
        json_at_time = at_time.isoformat() if at_time else None

    params["$at-time"] = json_at_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]:
    if response.status_code == 200:
        response_200 = ReadMetaRT.from_dict(response.json())

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
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]:
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
    schema_filter: Union[Unset, None, str] = UNSET,
    at_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]:
    """read metadata

     Return a list of metadata records attached to an entity.

    Args:
        entity_id (str): Entity for which to request metadata Example: urn:blue:image.collA.12.
        schema_filter (Union[Unset, None, str]): Optional comma separated list of schemas to
            filter on Example: urn:blue:image,urn:blue:location.
        at_time (Union[Unset, None, datetime.datetime]): Return metadata which where valid at that
            time [now] Example: 1996-12-19T16:39:57-08:00.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        client=client,
        schema_filter=schema_filter,
        at_time=at_time,
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
    schema_filter: Union[Unset, None, str] = UNSET,
    at_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]:
    """read metadata

     Return a list of metadata records attached to an entity.

    Args:
        entity_id (str): Entity for which to request metadata Example: urn:blue:image.collA.12.
        schema_filter (Union[Unset, None, str]): Optional comma separated list of schemas to
            filter on Example: urn:blue:image,urn:blue:location.
        at_time (Union[Unset, None, datetime.datetime]): Return metadata which where valid at that
            time [now] Example: 1996-12-19T16:39:57-08:00.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]
    """

    return sync_detailed(
        entity_id=entity_id,
        client=client,
        schema_filter=schema_filter,
        at_time=at_time,
    ).parsed


async def asyncio_detailed(
    entity_id: str,
    *,
    client: AuthenticatedClient,
    schema_filter: Union[Unset, None, str] = UNSET,
    at_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]:
    """read metadata

     Return a list of metadata records attached to an entity.

    Args:
        entity_id (str): Entity for which to request metadata Example: urn:blue:image.collA.12.
        schema_filter (Union[Unset, None, str]): Optional comma separated list of schemas to
            filter on Example: urn:blue:image,urn:blue:location.
        at_time (Union[Unset, None, datetime.datetime]): Return metadata which where valid at that
            time [now] Example: 1996-12-19T16:39:57-08:00.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        client=client,
        schema_filter=schema_filter,
        at_time=at_time,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    entity_id: str,
    *,
    client: AuthenticatedClient,
    schema_filter: Union[Unset, None, str] = UNSET,
    at_time: Union[Unset, None, datetime.datetime] = UNSET,
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]:
    """read metadata

     Return a list of metadata records attached to an entity.

    Args:
        entity_id (str): Entity for which to request metadata Example: urn:blue:image.collA.12.
        schema_filter (Union[Unset, None, str]): Optional comma separated list of schemas to
            filter on Example: urn:blue:image,urn:blue:location.
        at_time (Union[Unset, None, datetime.datetime]): Return metadata which where valid at that
            time [now] Example: 1996-12-19T16:39:57-08:00.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ReadMetaRT]]
    """

    return (
        await asyncio_detailed(
            entity_id=entity_id,
            client=client,
            schema_filter=schema_filter,
            at_time=at_time,
        )
    ).parsed
