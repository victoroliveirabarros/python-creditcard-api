from http import HTTPStatus
import jwt
from fastapi import APIRouter, Request, Response, Depends, Header

from app.domain.usecases import (CreditCardParams,
                                 UserParams,
                                 UserLoginParams)
from app.main.adapter import fastapi_adapter
from app.main.auth import token_required
from app.main.factories import (create_credit_card_factory,
                                create_user_factory,
                                list_credit_cards_factory,
                                get_credit_card_factory,
                                user_login_factory)
from app.services.helpers.helpers import SECRET_KEY
from app.services.helpers.http import HttpResponse

SECRET_KEY = 'maistodos'

router = APIRouter(
    prefix='/api/v1',
    responses={
        HTTPStatus.BAD_REQUEST.value: {
            'description': 'Erro ao cadastrar cartão',
        },
        HTTPStatus.NOT_FOUND.value: {
            'description': 'Device não encontrado',
        }
    },
    tags=['Cards']
)

@router.post('/credit-card')
def add_credit_card(
    body: CreditCardParams,
    request: Request,
    response: Response
):
    return fastapi_adapter(body, response, create_credit_card_factory())

@router.get('/credit-card')
@token_required
def list_credit_cards(
    request: Request,
    response: Response
):
    return fastapi_adapter(None, response, list_credit_cards_factory())

@router.get('/credit-card/{id_card}')
def get_credit_card(
    id_card: int,
    request: Request,
    response: Response
):
    return fastapi_adapter(None, response, get_credit_card_factory(id_card))

user_route = APIRouter(
    prefix='/api/v1',
    tags=['Users']
)

@user_route.post('/user')
def create_user(
    body: UserParams,
    request: Request,
    response: Response
):
    return fastapi_adapter(body, response, create_user_factory())

@user_route.post('/signin')
def user_login(
    body: UserLoginParams,
    request: Request,
    response: Response
):
    return fastapi_adapter(body, response, user_login_factory())
