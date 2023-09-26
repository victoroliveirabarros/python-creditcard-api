from http import HTTPStatus
from functools import wraps
import jwt
from typing import Dict
from app.services.helpers.helpers import SECRET_KEY

SECRET_KEY = 'maistodos'

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        
        request = kwargs.get('request', None)
        response: object = kwargs.get('response', None)
        
        try:
            headers: Dict = getattr(request, 'headers', {})

            if not headers.get('Authorization'):
                 print(headers.get('Authorization'))
                 response.status_code = HTTPStatus.UNAUTHORIZED # type: ignore
                 return response
            
            token = headers.get('Authorization').split("Bearer ")[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            #current_user = get_user_by_id(data['user_id'])  # Substitua por sua função de obtenção de usuário
        
        except jwt.ExpiredSignatureError:
            response.status_code = HTTPStatus.UNAUTHORIZED # type: ignore
            return response
        except jwt.InvalidTokenError:
            response.status_code = HTTPStatus.UNAUTHORIZED # type: ignore
            return response

        return func(*args, **kwargs)

    return decorated
