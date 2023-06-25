

from http.client import HTTPException
from .types import Response
from .excpetions import NotAuthorizedException
from urllib.parse import urlparse

def process_error(method: str, r: Response, verbose: bool = True):
    if verbose:
        print(f"Error: {method} failed with {r.status_code} - {r.content}")
    if r.status_code == 401:
        raise NotAuthorizedException()
    raise HTTPException(r.status_code, r.content)

def set_page(next: str):
    u = urlparse(next)
    q = u.query
    if q.startswith("page="):
        return q[len("page="):]
    else:
        raise Exception(f"unexpected 'next' link format - {q}")
