from functools import wraps
from http import HTTPStatus
from typing import Dict

import jwt
from sqlalchemy.orm import sessionmaker

from app.domain.models import User
from app.infra.database import engine
from app.services.helpers.helpers import SECRET_KEY


def check_user_is_admin(user_id) -> bool:
    Session = sessionmaker(bind=engine)

    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    session.close()

    if user.is_admin:
        return True
    return False


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):

        request = kwargs.get('request', None)
        response: object = kwargs.get('response', None)

        try:
            headers: Dict = getattr(request, 'headers', {})

            if not headers.get('Authorization'):
                print(headers.get('Authorization'))
                response.status_code = HTTPStatus.UNAUTHORIZED  # type: ignore
                return response

            token = headers.get('Authorization').split("Bearer ")[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            is_admin = check_user_is_admin(data['user_id'])

        except jwt.ExpiredSignatureError:
            response.status_code = HTTPStatus.UNAUTHORIZED  # type: ignore
            return response
        except jwt.InvalidTokenError:
            response.status_code = HTTPStatus.UNAUTHORIZED  # type: ignore
            return response

        return func(is_admin, *args, **kwargs)

    return decorated


def admin_required(func):
    @wraps(func)
    def decorated(is_admin, *args, **kwargs):
        response: object = kwargs.get('response', None)
        if not is_admin:
            response.status_code = HTTPStatus.FORBIDDEN  # type: ignore
            return response
        return func(*args, **kwargs)

    return decorated
