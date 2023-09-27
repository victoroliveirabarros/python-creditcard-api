# test_get_credit_card_usecase.py
import datetime
from http import HTTPStatus

from app.domain.models import CreditCardModel
from app.services.usecases import GetCreditCardUsecase
from unittest.mock import MagicMock

class TestGetCreditCardUsecase:

    def test_execute_with_existing_card(self):
        session_mock = MagicMock()
        usecase = GetCreditCardUsecase(session_mock, id_card=1)

        card_data = {
            'id': 1,
            'exp_date': datetime.datetime.strptime('2023-12-31', '%Y-%m-%d').strftime('%Y-%m-%d'),
            'holder': 'John Doe',
            'number': '4111111111111111',
            'cvv': '123',
            'brand': 'Visa'
        }
        
        session_mock.query.return_value.filter_by.return_value.first.return_value = CreditCardModel(**card_data)

        response = usecase.execute(params=None)

        assert response.status_code == HTTPStatus.OK

    def test_execute_with_non_existing_card(self):
        session_mock = MagicMock()
        usecase = GetCreditCardUsecase(session_mock)

        session_mock.query.return_value.filter_by.return_value.first.return_value = None

        response = usecase.execute(params=None)

        assert response.status_code == HTTPStatus.NOT_FOUND
