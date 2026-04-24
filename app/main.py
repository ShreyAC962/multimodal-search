from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from app.api import search

app = FastAPI()

app.include_router(search.router)
