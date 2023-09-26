from sqlalchemy.orm import sessionmaker

from app.domain.usecases import Usecase
from app.infra.database import engine
from app.services.usecases import (CreateCreditCardUsecase,
                                   ListCreditCardsUsecase,
                                   GetCreditCardUsecase,
                                   CreateUserUsecase)

def create_credit_card_factory() -> Usecase:
    Session = sessionmaker(bind=engine)

    return CreateCreditCardUsecase(
        session=Session
    )

def list_credit_cards_factory() -> Usecase:
    Session = sessionmaker(bind=engine)

    return ListCreditCardsUsecase(
        session=Session
    )

def get_credit_card_factory(id_card: int) -> Usecase:
    Session = sessionmaker(bind=engine)

    return GetCreditCardUsecase(
        session=Session,
        id_card=id_card
    )

def create_user_factory() -> Usecase:
    Session = sessionmaker(bind=engine)

    return CreateUserUsecase(
        session=Session
    )
