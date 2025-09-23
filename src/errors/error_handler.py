from src.presentation.http_types.http_response import HTTPResponse
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_forbidden import HttpForbiddenError
from src.errors.types.http_confit_error import HttpConflictError
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.types.validation_error import ValidationError
from src.errors.types.http_internal_serverEerror import HttpInternalServerError
def handle_errors(error:Exception)-> HTTPResponse:
    if isinstance(error,(
        HttpBadRequestError,
        HttpForbiddenError,
        HttpConflictError,
        HttpNotFoundError,
        ValidationError,
        HttpUnprocessableEntityError,
        HttpInternalServerError
    )):
        return HTTPResponse(
            status_code=error.status_code,
            body={"error":[
                {
                    "title":error.name,
                    "message":error.message
                }
            ]}
        )
    return HTTPResponse(
        status_code=500,
        body={"error":[
            {
                "title":"Internal Server Error",
                "message":"An internal server error occurred"
            }
        ]}
    )