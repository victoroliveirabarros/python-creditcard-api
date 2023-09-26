from http import HTTPStatus
import datetime

from app.domain.models import User
from app.domain.usecases import UserLoginContract, UserLoginParams

from app.services.helpers.http.http import HttpResponse
from app.services.helpers import create_token


class UserLoginUsecase(UserLoginContract):

    def __init__(
        self,
        session
    ) -> None:
        self.session = session

    def execute(self, params: UserLoginParams) -> HttpResponse:
        username = params.username
        password = params.password

        print('entrou aqui')

        session = self.session()

        if not username or not password:
            return HttpResponse(HTTPStatus.BAD_REQUEST, {'message': 'Username and password are required'})

        # Verifique se o usuário já existe
        existing_user = session.query(User).filter_by(username=username, password=password).first()
        if existing_user:
            token = create_token(existing_user.id)
            return HttpResponse(HTTPStatus.OK, {'token': token})

        return HttpResponse(HTTPStatus.UNAUTHORIZED, {'message': 'Username or password incorrect'})
