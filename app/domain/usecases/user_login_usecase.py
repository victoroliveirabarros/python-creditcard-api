from abc import abstractmethod

from app.services.helpers.http import HttpResponse

from .usecase import InputData, Usecase


class UserLoginParams(InputData):
    username: str
    password: str


class UserLoginContract(Usecase):
    @abstractmethod
    def execute(self, params: UserLoginParams, session) -> HttpResponse:
        raise NotImplementedError()
