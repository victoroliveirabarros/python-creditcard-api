from http import HTTPStatus
from typing import Any, Dict, Optional

from fastapi import Response


class HttpRequest:
    def __init__(self, header: Optional[Dict] = None, body: Optional[Dict] = None, query: Optional[Dict] = None):
        self.header = header
        self.body = body
        self.query = query

    def __repr__(self):
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query})"
        )


class HttpResponse:

    def __init__(self, status_code: int, body: Any = None, headers: Dict[str, str | int] | None = None):
        self.status_code = status_code
        self.body = body
        self.headers = headers

    def __repr__(self):
        return f"HttpResponse (status_code={self.status_code}, body={self.body}), headers={self.headers}"


class HttpError(Exception):
    def __init__(
        self,
        status_code: int,
        message: str = HTTPStatus.INTERNAL_SERVER_ERROR.phrase
    ):
        self.status_code = status_code
        self.message = message

    def __repr__(self):
        return f'HttpError (status_code={self.status_code}, message={self.message})'


class HttpStatus:
    @staticmethod
    def ok_200(body: Optional[Any] = None, headers: Dict[str, str | int] | None = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.OK, body, headers=headers)

    @staticmethod
    def created_201(body: Optional[Any] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.CREATED, body)

    @staticmethod
    def accepted_202(body: Optional[Any] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.ACCEPTED, body)

    @staticmethod
    def no_content_204() -> HttpResponse:
        return HttpResponse(HTTPStatus.NO_CONTENT)

    @staticmethod
    def bad_request_400(custom_msg: Optional[str] = None, body: Any = None) -> HttpResponse:
        if body:
            return HttpResponse(HTTPStatus.BAD_REQUEST, body)
        return HttpResponse(HTTPStatus.BAD_REQUEST, {"error": custom_msg or "Bad Request"})

    @staticmethod
    def unauthorized_401(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.UNAUTHORIZED, {"error": custom_msg or "Unauthorized"})

    @staticmethod
    def forbidden_403(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.FORBIDDEN, {"error": custom_msg or "Forbidden"})

    @staticmethod
    def not_found_404(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.NOT_FOUND, {"error": custom_msg or "Not Found"})

    @staticmethod
    def not_allowed_405(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.METHOD_NOT_ALLOWED, {"error": custom_msg or "Method Not Allowed"})

    @staticmethod
    def not_acceptable_406(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.NOT_ACCEPTABLE, {"error": custom_msg or "Not Acceptable"})

    @staticmethod
    def conflict_409(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.CONFLICT, {"error": custom_msg or "Conflict"})

    @staticmethod
    def precondition_failed_412(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.PRECONDITION_FAILED, {"error": custom_msg or "Precondition Failed"})

    @staticmethod
    def expection_failed_417(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.EXPECTATION_FAILED, {"error": custom_msg or "Expectation Failed"})

    @staticmethod
    def im_a_teapot_418(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.IM_A_TEAPOT, {"error": custom_msg or "Im a Teapot"})  # pylint: disable=no-member

    @staticmethod
    def unprocessable_entity_422(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.UNPROCESSABLE_ENTITY, {"error": custom_msg or "Unprocessable Entity"})

    @staticmethod
    def locked_423(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.LOCKED, {"error": custom_msg or "Resource Locked"})

    @staticmethod
    def internal_server_error_500(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": custom_msg or "Internal Server Error"})

    @staticmethod
    def not_implemented_error_501(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.NOT_IMPLEMENTED, {"error": custom_msg or "Not implemented Error"})

    @staticmethod
    def bad_gateway_502(custom_msg: Optional[str] = None, body: Any = None) -> HttpResponse:
        response_body = {
            "error": custom_msg or HTTPStatus.BAD_GATEWAY.description
        }
        if body:
            response_body = body
        return HttpResponse(
            status_code=HTTPStatus.BAD_GATEWAY.value,
            body=response_body
        )

    @staticmethod
    def service_unavailable_503(custom_msg: Optional[str] = None, body: Any = None) -> HttpResponse:
        response_body = {
            "error": custom_msg or HTTPStatus.SERVICE_UNAVAILABLE.description
        }
        if body:
            response_body = body
        return HttpResponse(
            HTTPStatus.SERVICE_UNAVAILABLE.value,
            response_body
        )

    @staticmethod
    def gateway_timeout_504(custom_msg: Optional[str] = None) -> HttpResponse:
        return HttpResponse(HTTPStatus.GATEWAY_TIMEOUT, {"error": custom_msg or "Internal Server Error"})


def set_response(
    status_code: int,
    response: Response,
    result: Optional[Any] = None,
    headers: Dict[str, str] | None = None,
) -> Response | Any:
    response.status_code = status_code
    if headers:
        response.headers.update({key: value for key, value in headers.items()})
    return result or response
