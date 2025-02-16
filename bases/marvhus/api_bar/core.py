from marvhus.log import get_logger
import marvhus.math_utils as mu
from fastapi import FastAPI

logger = get_logger("api-bar")
app = FastAPI()

@app.get("/fib/{index}")
async def fib(index: int) -> dict:
    logger.info(f"Got request to calculate fibonachi number for index {index}")

    logger.info(f"math_utils: {mu}")
    result = mu.fib(index)

    return {
        "success": not result is None,
        "value": result,
    }
