from http import HTTPStatus

from app.domain.models import CreditCardModel
from app.domain.usecases import CreditCardParams
from app.services.usecases import CreateCreditCardUsecase
from unittest.mock import MagicMock
from faker import Faker

fake = Faker()

class TestCreateCreditCardUsecase:

    def test_execute_with_valid_params(self):
        session_mock = MagicMock()
        usecase = CreateCreditCardUsecase(session_mock)

        exp_date = fake.future_date(end_date='+10y', tzinfo=None).strftime('%m/%Y')
        holder = fake.name()
        number = fake.credit_card_number(card_type='mastercard')
        cvv = fake.random_int(min=100, max=999)

        params = CreditCardParams(
            exp_date=exp_date,
            number=number,
            holder=holder,
            cvv=cvv
        )

        response = usecase.execute(params)

        assert response.status_code == HTTPStatus.CREATED

    def test_execute_with_invalid_exp_date(self):
        session_mock = MagicMock()
        usecase = CreateCreditCardUsecase(session_mock)

        exp_date = '13/2023'  # Mês inválido
        holder = fake.name()
        number = fake.credit_card_number(card_type='mastercard')
        cvv = fake.random_int(min=100, max=999)

        params = CreditCardParams(
            exp_date=exp_date,
            number=number,
            holder=holder,
            cvv=cvv
        )

        response = usecase.execute(params)

        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_execute_with_invalid_card_number(self):
        session_mock = MagicMock()
        usecase = CreateCreditCardUsecase(session_mock)

        exp_date = fake.future_date(end_date='+10y', tzinfo=None).strftime('%m/%Y')
        holder = fake.name()
        number = '80555158112'
        cvv = fake.random_int(min=100, max=999)

        params = CreditCardParams(
            exp_date=exp_date,
            number=number,
            holder=holder,
            cvv=cvv
        )

        response = usecase.execute(params)

        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_execute_with_invalid_holder(self):
        session_mock = MagicMock()
        usecase = CreateCreditCardUsecase(session_mock)

        exp_date = fake.future_date(end_date='+10y', tzinfo=None).strftime('%m/%Y')
        holder = 'A'
        number = fake.credit_card_number(card_type='mastercard')
        cvv = fake.random_int(min=100, max=999)

        params = CreditCardParams(
            exp_date=exp_date,
            number=number,
            holder=holder,
            cvv=cvv
        )

        response = usecase.execute(params)

        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_execute_with_invalid_cvv(self):
        session_mock = MagicMock()
        usecase = CreateCreditCardUsecase(session_mock)

        exp_date = fake.future_date(end_date='+10y', tzinfo=None).strftime('%m/%Y')
        holder = fake.name()
        number = fake.credit_card_number(card_type='mastercard')
        cvv = 8

        params = CreditCardParams(
            exp_date=exp_date,
            number=number,
            holder=holder,
            cvv=cvv
        )

        response = usecase.execute(params)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        
