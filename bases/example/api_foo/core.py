from example.log import get_logger
from example.service_foo import retrieve_some_data
from fastapi import FastAPI

logger = get_logger("api-foo-logger")
app = FastAPI()

@app.get("/")
async def root() -> dict:
    logger.info("The FastAPI root endpoint was called.")

    return {"message": "Foo"}

@app.get("/data/{key}")
async def data(key: str) -> dict:
    logger.info(f"Got request to retrieve data for {key}")

    values = retrieve_some_data(key)

    return {
        "success": not values == None,
        "values": values,
    }
