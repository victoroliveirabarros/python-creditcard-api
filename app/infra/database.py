from sqlalchemy import create_engine

from app.domain.models import Base

# Create an SQLite database
DATABASE_URL = 'postgresql://postgres:postgres@postgres/creditcard'
engine = create_engine(DATABASE_URL)

# Create tables based on the models
Base.metadata.create_all(engine)
