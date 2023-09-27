from http import HTTPStatus

from app.domain.models import CreditCardModel
from app.domain.usecases import CreateCreditCardContract, CreditCardParams
from app.services.helpers import (
    encrypt_credit_card_number,
    format_exp_date,
    get_card_brand,
    validate_credit_card_number,
    validate_exp_date,
    validate_holder,
)
from app.services.helpers.http.http import HttpResponse


class CreateCreditCardUsecase(CreateCreditCardContract):

    def __init__(
        self,
        session
    ) -> None:
        self.session = session

    def execute(self, params: CreditCardParams) -> HttpResponse:
        exp_date = params.exp_date
        holder = params.holder
        number = params.number
        cvv = params.cvv

        if not validate_exp_date(exp_date):
            return HttpResponse(HTTPStatus.BAD_REQUEST, 'Invalid expiration date')

        if not validate_holder(holder):
            return HttpResponse(HTTPStatus.BAD_REQUEST, 'Invalid holder name')

        if cvv and not (3 <= len(str(cvv)) <= 4 and str(cvv).isdigit()):
            return HttpResponse(HTTPStatus.BAD_REQUEST, 'Invalid CVV')

        if not validate_credit_card_number(number):
            return HttpResponse(HTTPStatus.BAD_REQUEST, 'Invalid credit card number')

        # Create a new CreditCard object
        new_credit_card = CreditCardModel(
            exp_date=format_exp_date(exp_date),
            holder=holder,
            number=encrypt_credit_card_number(number),
            cvv=cvv,
            brand=get_card_brand(number)
        )

        # Add the new credit card to the database
        session = self.session()
        session.add(new_credit_card)
        session.commit()
        session.close()

        return HttpResponse(HTTPStatus.CREATED, 'Credit card added successfully')
