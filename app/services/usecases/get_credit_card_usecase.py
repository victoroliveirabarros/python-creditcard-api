import datetime
from http import HTTPStatus

from app.domain.models import CreditCardModel
from app.domain.usecases import Usecase
from app.services.helpers.http.http import HttpResponse


class GetCreditCardUsecase(Usecase):

    def __init__(
        self,
        session,
        id_card=None
    ) -> None:
        self.session = session
        self.id_card = id_card

    def execute(self, params: None) -> HttpResponse:
        if not self.id_card:
            return HttpResponse(HTTPStatus.NOT_FOUND, 'Card id is missing')

        session = self.session()

        # Retrieve the credit card with the specified ID from the database
        credit_card = session.query(CreditCardModel).filter_by(id=self.id_card).first()

        session.close()

        if credit_card is not None:
            credit_card_data = {
                'id': credit_card.id,
                'exp_date': credit_card.exp_date,
                'holder': credit_card.holder,
                'number': credit_card.number,
                'cvv': credit_card.cvv,
                'brand': credit_card.brand
            }
            return HttpResponse(HTTPStatus.OK, credit_card_data)

        return HttpResponse(HTTPStatus.NOT_FOUND, 'Card Not Found')
