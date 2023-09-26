from http import HTTPStatus
from fastapi import APIRouter, Request, Response

from app.domain.usecases import CreditCardParams, UserParams
from app.main.adapter import fastapi_adapter
from app.main.factories import (create_credit_card_factory,
                                create_user_factory,
                                list_credit_cards_factory,
                                get_credit_card_factory)

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
    response: Response
):
    return fastapi_adapter(body, response, create_credit_card_factory())

@router.get('/credit-card')
def list_credit_cards(
    response: Response
):
    return fastapi_adapter(None, response, list_credit_cards_factory())

@router.get('/credit-card/{id_card}')
def get_credit_card(
    id_card: int,
    response: Response
):
    print("entrei aqui")
    return fastapi_adapter(None, response, get_credit_card_factory(id_card))

user_route = APIRouter(
    prefix='/api/v1',
    tags=['Users']
)

@user_route.post('/user')
def create_user(
    body: UserParams,
    response: Response
):
    return fastapi_adapter(body, response, create_user_factory())
