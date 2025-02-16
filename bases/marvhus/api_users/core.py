from fastapi import FastAPI
from marvhus.log import get_logger

logger = get_logger("api_users")
app = FastAPI()
