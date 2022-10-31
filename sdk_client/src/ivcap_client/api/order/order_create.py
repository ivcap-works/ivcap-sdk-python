from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.invalid_parameter_value import InvalidParameterValue
from ...models.invalid_scopes_t import InvalidScopesT
from ...models.not_implemented_t import NotImplementedT
from ...models.order_request_t import OrderRequestT
from ...models.order_status_rt import OrderStatusRT
from ...models.resource_not_found_t import ResourceNotFoundT
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: OrderRequestT,
) -> Dict[str, Any]:
    url = "{}/1/orders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]:
    if response.status_code == 200:
        response_200 = OrderStatusRT.from_dict(response.json())

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
    if response.status_code == 422:
        response_422 = InvalidParameterValue.from_dict(response.json())

        return response_422
    if response.status_code == 501:
        response_501 = NotImplementedT.from_dict(response.json())

        return response_501
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: OrderRequestT,
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]:
    """create order

     Create a new orders and return its status.

    Args:
        json_body (OrderRequestT):  Example: {'accountID': '123e4567-e89b-12d3-a456-426614174000',
            'metadata': {'refID': '33-444'}, 'name': 'Fire risk for Lot2', 'parameters': [{'name':
            'region', 'value': 'Upper Valley'}, {'name': 'threshold', 'value': 10}], 'serviceID':
            '123e4567-e89b-12d3-a456-426614174000'}.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: OrderRequestT,
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]:
    """create order

     Create a new orders and return its status.

    Args:
        json_body (OrderRequestT):  Example: {'accountID': '123e4567-e89b-12d3-a456-426614174000',
            'metadata': {'refID': '33-444'}, 'name': 'Fire risk for Lot2', 'parameters': [{'name':
            'region', 'value': 'Upper Valley'}, {'name': 'threshold', 'value': 10}], 'serviceID':
            '123e4567-e89b-12d3-a456-426614174000'}.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: OrderRequestT,
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]:
    """create order

     Create a new orders and return its status.

    Args:
        json_body (OrderRequestT):  Example: {'accountID': '123e4567-e89b-12d3-a456-426614174000',
            'metadata': {'refID': '33-444'}, 'name': 'Fire risk for Lot2', 'parameters': [{'name':
            'region', 'value': 'Upper Valley'}, {'name': 'threshold', 'value': 10}], 'serviceID':
            '123e4567-e89b-12d3-a456-426614174000'}.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: OrderRequestT,
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]:
    """create order

     Create a new orders and return its status.

    Args:
        json_body (OrderRequestT):  Example: {'accountID': '123e4567-e89b-12d3-a456-426614174000',
            'metadata': {'refID': '33-444'}, 'name': 'Fire risk for Lot2', 'parameters': [{'name':
            'region', 'value': 'Upper Valley'}, {'name': 'threshold', 'value': 10}], 'serviceID':
            '123e4567-e89b-12d3-a456-426614174000'}.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, OrderStatusRT, ResourceNotFoundT]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
