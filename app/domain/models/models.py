from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CreditCardModel(Base):
    __tablename__ = 'credit_cards'

    id = Column(Integer, primary_key=True)
    exp_date = Column(String)
    holder = Column(String)
    number = Column(String)
    cvv = Column(String)
    brand = Column(String)
