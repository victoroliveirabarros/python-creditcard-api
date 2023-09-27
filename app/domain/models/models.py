from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CreditCardModel(Base):
    __tablename__ = 'credit_cards'

    id = Column(Integer, primary_key=True)
    exp_date = Column(String)
    holder = Column(String(50))
    number = Column(String)
    cvv = Column(String)
    brand = Column(String)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_admin = is_admin
