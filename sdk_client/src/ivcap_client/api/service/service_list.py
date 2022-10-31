from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.not_implemented_t import NotImplementedT
from ...models.service_list_rt import ServiceListRT
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = "",
    orderby: Union[Unset, None, str] = "",
    top: Union[Unset, None, int] = 10,
    skip: Union[Unset, None, int] = 0,
    select: Union[Unset, None, str] = "",
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = "",
) -> Dict[str, Any]:
    url = "{}/1/services".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["$filter"] = filter_

    params["$orderby"] = orderby

    params["$top"] = top

    params["$skip"] = skip

    params["$select"] = select

    params["offset"] = offset

    params["limit"] = limit

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, NotImplementedT, ServiceListRT]]:
    if response.status_code == 200:
        response_200 = ServiceListRT.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 501:
        response_501 = NotImplementedT.from_dict(response.json())

        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, NotImplementedT, ServiceListRT]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = "",
    orderby: Union[Unset, None, str] = "",
    top: Union[Unset, None, int] = 10,
    skip: Union[Unset, None, int] = 0,
    select: Union[Unset, None, str] = "",
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = "",
) -> Response[Union[Any, NotImplementedT, ServiceListRT]]:
    """list service

     services

    Args:
        filter_ (Union[Unset, None, str]): The $filter system query option allows clients to
            filter a collection of
                                        resources that are addressed by a request URL. The expression specified with $filter
                                        is evaluated for each resource in the collection, and only items where the expression
                                        evaluates to true are included in the response. Default: ''. Example:
            $filter=FirstName eq 'Scott'.
        orderby (Union[Unset, None, str]): The $orderby query option allows clients to request
            resources in either
                                        ascending order using asc or descending order using desc. If asc or desc not
            specified,
                                        then the resources will be ordered in ascending order. The request below orders Trips
            on
                                        property EndsAt in descending order. Default: ''. Example: $orderby=EndsAt desc.
        top (Union[Unset, None, int]): The $top system query option requests the number of items
            in the queried
                                        collection to be included in the result. Default: 10. Example: 10.
        skip (Union[Unset, None, int]): The $skip query option requests the number of items in the
            queried collection
                                        that are to be skipped and not included in the result.
        select (Union[Unset, None, str]): The $select system query option allows the clients to
            requests a limited set
                                        of properties for each entity or complex type. The example returns Name and IcaoCode
                                        of all Airports. Default: ''. Example: $select=Name, IcaoCode.
        offset (Union[Unset, None, int]): DEPRECATED: List offset
        limit (Union[Unset, None, int]): DEPRECATED: Max. number of records to return Example: 10.
        page_token (Union[Unset, None, str]): DEPRECATED: Page token Default: ''.

    Returns:
        Response[Union[Any, NotImplementedT, ServiceListRT]]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        orderby=orderby,
        top=top,
        skip=skip,
        select=select,
        offset=offset,
        limit=limit,
        page_token=page_token,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = "",
    orderby: Union[Unset, None, str] = "",
    top: Union[Unset, None, int] = 10,
    skip: Union[Unset, None, int] = 0,
    select: Union[Unset, None, str] = "",
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = "",
) -> Optional[Union[Any, NotImplementedT, ServiceListRT]]:
    """list service

     services

    Args:
        filter_ (Union[Unset, None, str]): The $filter system query option allows clients to
            filter a collection of
                                        resources that are addressed by a request URL. The expression specified with $filter
                                        is evaluated for each resource in the collection, and only items where the expression
                                        evaluates to true are included in the response. Default: ''. Example:
            $filter=FirstName eq 'Scott'.
        orderby (Union[Unset, None, str]): The $orderby query option allows clients to request
            resources in either
                                        ascending order using asc or descending order using desc. If asc or desc not
            specified,
                                        then the resources will be ordered in ascending order. The request below orders Trips
            on
                                        property EndsAt in descending order. Default: ''. Example: $orderby=EndsAt desc.
        top (Union[Unset, None, int]): The $top system query option requests the number of items
            in the queried
                                        collection to be included in the result. Default: 10. Example: 10.
        skip (Union[Unset, None, int]): The $skip query option requests the number of items in the
            queried collection
                                        that are to be skipped and not included in the result.
        select (Union[Unset, None, str]): The $select system query option allows the clients to
            requests a limited set
                                        of properties for each entity or complex type. The example returns Name and IcaoCode
                                        of all Airports. Default: ''. Example: $select=Name, IcaoCode.
        offset (Union[Unset, None, int]): DEPRECATED: List offset
        limit (Union[Unset, None, int]): DEPRECATED: Max. number of records to return Example: 10.
        page_token (Union[Unset, None, str]): DEPRECATED: Page token Default: ''.

    Returns:
        Response[Union[Any, NotImplementedT, ServiceListRT]]
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        orderby=orderby,
        top=top,
        skip=skip,
        select=select,
        offset=offset,
        limit=limit,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = "",
    orderby: Union[Unset, None, str] = "",
    top: Union[Unset, None, int] = 10,
    skip: Union[Unset, None, int] = 0,
    select: Union[Unset, None, str] = "",
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = "",
) -> Response[Union[Any, NotImplementedT, ServiceListRT]]:
    """list service

     services

    Args:
        filter_ (Union[Unset, None, str]): The $filter system query option allows clients to
            filter a collection of
                                        resources that are addressed by a request URL. The expression specified with $filter
                                        is evaluated for each resource in the collection, and only items where the expression
                                        evaluates to true are included in the response. Default: ''. Example:
            $filter=FirstName eq 'Scott'.
        orderby (Union[Unset, None, str]): The $orderby query option allows clients to request
            resources in either
                                        ascending order using asc or descending order using desc. If asc or desc not
            specified,
                                        then the resources will be ordered in ascending order. The request below orders Trips
            on
                                        property EndsAt in descending order. Default: ''. Example: $orderby=EndsAt desc.
        top (Union[Unset, None, int]): The $top system query option requests the number of items
            in the queried
                                        collection to be included in the result. Default: 10. Example: 10.
        skip (Union[Unset, None, int]): The $skip query option requests the number of items in the
            queried collection
                                        that are to be skipped and not included in the result.
        select (Union[Unset, None, str]): The $select system query option allows the clients to
            requests a limited set
                                        of properties for each entity or complex type. The example returns Name and IcaoCode
                                        of all Airports. Default: ''. Example: $select=Name, IcaoCode.
        offset (Union[Unset, None, int]): DEPRECATED: List offset
        limit (Union[Unset, None, int]): DEPRECATED: Max. number of records to return Example: 10.
        page_token (Union[Unset, None, str]): DEPRECATED: Page token Default: ''.

    Returns:
        Response[Union[Any, NotImplementedT, ServiceListRT]]
    """

    kwargs = _get_kwargs(
        client=client,
        filter_=filter_,
        orderby=orderby,
        top=top,
        skip=skip,
        select=select,
        offset=offset,
        limit=limit,
        page_token=page_token,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    filter_: Union[Unset, None, str] = "",
    orderby: Union[Unset, None, str] = "",
    top: Union[Unset, None, int] = 10,
    skip: Union[Unset, None, int] = 0,
    select: Union[Unset, None, str] = "",
    offset: Union[Unset, None, int] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    page_token: Union[Unset, None, str] = "",
) -> Optional[Union[Any, NotImplementedT, ServiceListRT]]:
    """list service

     services

    Args:
        filter_ (Union[Unset, None, str]): The $filter system query option allows clients to
            filter a collection of
                                        resources that are addressed by a request URL. The expression specified with $filter
                                        is evaluated for each resource in the collection, and only items where the expression
                                        evaluates to true are included in the response. Default: ''. Example:
            $filter=FirstName eq 'Scott'.
        orderby (Union[Unset, None, str]): The $orderby query option allows clients to request
            resources in either
                                        ascending order using asc or descending order using desc. If asc or desc not
            specified,
                                        then the resources will be ordered in ascending order. The request below orders Trips
            on
                                        property EndsAt in descending order. Default: ''. Example: $orderby=EndsAt desc.
        top (Union[Unset, None, int]): The $top system query option requests the number of items
            in the queried
                                        collection to be included in the result. Default: 10. Example: 10.
        skip (Union[Unset, None, int]): The $skip query option requests the number of items in the
            queried collection
                                        that are to be skipped and not included in the result.
        select (Union[Unset, None, str]): The $select system query option allows the clients to
            requests a limited set
                                        of properties for each entity or complex type. The example returns Name and IcaoCode
                                        of all Airports. Default: ''. Example: $select=Name, IcaoCode.
        offset (Union[Unset, None, int]): DEPRECATED: List offset
        limit (Union[Unset, None, int]): DEPRECATED: Max. number of records to return Example: 10.
        page_token (Union[Unset, None, str]): DEPRECATED: Page token Default: ''.

    Returns:
        Response[Union[Any, NotImplementedT, ServiceListRT]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            orderby=orderby,
            top=top,
            skip=skip,
            select=select,
            offset=offset,
            limit=limit,
            page_token=page_token,
        )
    ).parsed
