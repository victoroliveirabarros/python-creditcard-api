from http import HTTPStatus
import datetime

from app.domain.models import User
from app.domain.usecases import CreateUserContract, UserParams

from app.services.helpers.http.http import HttpResponse


class CreateUserUsecase(CreateUserContract):

    def __init__(
        self,
        session
    ) -> None:
        self.session = session

    def execute(self, params: UserParams) -> HttpResponse:
        username = params.username
        password = params.password
        is_admin = params.is_admin

        session = self.session()

        if not username or not password:
            return HttpResponse(HTTPStatus.BAD_REQUEST, {'message': 'Username and password are required'})

        # Verifique se o usuário já existe
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            return HttpResponse(HTTPStatus.BAD_REQUEST, {'message': 'Username already exists'})

        # Crie um novo usuário
        new_user = User(username=username, password=password, is_admin=is_admin)
        session.add(new_user)
        session.commit()

        return HttpResponse(HTTPStatus.CREATED, {'message': 'User created successfully'})
    