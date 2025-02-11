from example.log import get_logger
from fastapi import FastAPI

logger = get_logger("api-foo-logger")
app = FastAPI()

@app.get("/")
def root() -> dict:
    logger.info("The FastAPI root endpoint was called.")

    return {"message": "Foo"}
