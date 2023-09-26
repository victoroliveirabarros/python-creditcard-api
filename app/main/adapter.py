from http import HTTPStatus
from typing import Any, Optional

from fastapi import Response

from app.domain.usecases import Usecase
from app.services.helpers.http import HttpError


def fastapi_adapter(
    params: object,
    response: Response,
    usecase: Usecase
) -> Any:
    try:
        usecase_response = usecase.execute(params)
        response.status_code = usecase_response.status_code
        return usecase_response.body or response
    except HttpError as error:
        response.status_code = error.status_code
        return {'message': error.message} if error.message else response
    except Exception:
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return {'message': 'Internal server error'}
