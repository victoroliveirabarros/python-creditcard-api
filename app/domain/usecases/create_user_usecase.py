from abc import abstractmethod
from typing import Optional

from app.services.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class UserParams(InputData):
    username: Optional[str]
    password: Optional[str]
    is_admin: bool


class CreateUserContract(Usecase):
    @abstractmethod
    def execute(self, params: UserParams, session) -> HttpResponse:
        raise NotImplementedError()
