from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from fastapi import Request
from typing import Callable
from fastapi.responses import JSONResponse
async def request_adapter(request: Request, controller: Callable) -> HTTPResponse:
    body = {}
    if request.method in ["POST", "PUT", "PATCH"]:
        try:
            body = await request.json()
        except Exception:
            body = {}

    http_request = HTTPRequest(
        headers=dict(request.headers),
        query_params=dict(request.query_params),
        path_params=request.path_params,
        url=request.url.path,
        body=body
    )
    http_response = controller(http_request)
    return JSONResponse(
        status_code=http_response.status_code,
        content=http_response.body
    )