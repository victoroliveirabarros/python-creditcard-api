from abc import abstractmethod
from typing import Optional

from app.services.helpers.http import HttpResponse
from .usecase import Usecase, InputData


class CreditCardParams(InputData):
    exp_date: str
    number: str
    holder: str
    cvv: Optional[int]


class CreateCreditCardContract(Usecase):
    @abstractmethod
    def execute(self, params: CreditCardParams, session) -> HttpResponse:
        raise NotImplementedError()
