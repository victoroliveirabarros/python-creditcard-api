from http import HTTPStatus

from app.domain.models import CreditCardModel
from app.services.usecases import ListCreditCardsUsecase
from unittest.mock import MagicMock

class TestListCreditCardsUsecase:

    def test_execute_with_existing_cards(self):
        session_mock = MagicMock()
        usecase = ListCreditCardsUsecase(session_mock)

        # Mock para simular cartões existentes no banco de dados
        card_data = [
            {'id': 1, 'exp_date': '2023-12-31', 'holder': 'John Doe', 'number': '4111111111111111', 'cvv': '123', 'brand': 'Visa'},
            {'id': 2, 'exp_date': '2024-01-31', 'holder': 'Jane Doe', 'number': '5111111111111111', 'cvv': '456', 'brand': 'MasterCard'}
        ]
        session_mock.query.return_value.all.return_value = [CreditCardModel(**data) for data in card_data]

        response = usecase.execute(params=None)

        assert response.status_code == HTTPStatus.OK

    def test_execute_with_no_cards(self):
        session_mock = MagicMock()
        usecase = ListCreditCardsUsecase(session_mock)

        # Mock para simular nenhum cartão no banco de dados
        session_mock.query.return_value.all.return_value = []

        response = usecase.execute(params=None)

        assert response.status_code == HTTPStatus.OK
