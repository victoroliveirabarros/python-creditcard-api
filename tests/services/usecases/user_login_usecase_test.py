# test_user_login_usecase.py

from http import HTTPStatus

from app.domain.models import User
from app.domain.usecases import UserLoginParams
from app.services.usecases import UserLoginUsecase
from unittest.mock import MagicMock
from faker import Faker

fake = Faker()

class TestUserLoginUsecase:

    def test_execute_with_valid_credentials(self):
        session_mock = MagicMock()
        usecase = UserLoginUsecase(session_mock)

        username = fake.user_name()
        password = fake.password(length=12)

        session_mock.query.return_value.filter_by.return_value.first.return_value = User(username=username,password=password,is_admin=True)

        params = UserLoginParams(
            username=username,
            password=password
        )

        response = usecase.execute(params)

        assert response.status_code == HTTPStatus.OK

    def test_execute_with_missing_credentials(self):
        session_mock = MagicMock()
        usecase = UserLoginUsecase(session_mock)

        params = UserLoginParams(
            username='',
            password=''
        )

        response = usecase.execute(params)

        assert response.status_code == HTTPStatus.BAD_REQUEST
