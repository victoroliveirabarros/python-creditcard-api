# test_create_user_usecase.py

from http import HTTPStatus
from app.domain.models import User
from app.domain.usecases import UserParams
from app.services.usecases import CreateUserUsecase
from unittest.mock import MagicMock
from faker import Faker

fake = Faker()

class TestCreateUserUsecase:

    def test_execute_with_valid_params(self):
        session_mock = MagicMock()
        usecase = CreateUserUsecase(session_mock)

        username = fake.user_name()
        password = fake.password(length=12)
        is_admin = fake.boolean()

        params = UserParams(
            username=username,
            password=password,
            is_admin=is_admin
        )

        response = usecase.execute(params)

        assert response.status_code == HTTPStatus.BAD_REQUEST
