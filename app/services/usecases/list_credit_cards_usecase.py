import datetime
from http import HTTPStatus

from app.domain.models import CreditCardModel
from app.domain.usecases import Usecase
from app.services.helpers.http.http import HttpResponse


class ListCreditCardsUsecase(Usecase):

    def __init__(
        self,
        session
    ) -> None:
        self.session = session

    def execute(self, params: None) -> HttpResponse:
        session = self.session()

        # Retrieve all credit cards from the database
        credit_cards = session.query(CreditCardModel).all()

        session.close()

        # Convert credit card objects to dictionaries
        credit_cards_data = [
            {
                'id': card.id,
                'exp_date': datetime.datetime.strptime(card.exp_date, '%Y-%m-%d').strftime('%Y-%m-%d'),
                'holder': card.holder,
                'number': card.number,
                'cvv': card.cvv,
                'brand': card.brand
            }
            for card in credit_cards
        ]

        return HttpResponse(HTTPStatus.OK, credit_cards_data)
