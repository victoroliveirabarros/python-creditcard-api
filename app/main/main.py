# main.py
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from .routes import router, user_route

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI(
    title='Cards Service',
    description='Serviço de cadastro de cartões',
)

app.include_router(router)
app.include_router(user_route)
