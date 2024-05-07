import json
import logging
import logging.config
from fastapi import FastAPI, HTTPException
from logger import logger
from starlette.middleware.base import BaseHTTPMiddleware

# load logging configuration
with open('logging_config.json', 'r') as config_file:
    logging_config = json.load(config_file)
logging.config.dictConfig(logging_config)

# create logger
logger = logging.getLogger("my_app")

app = FastAPI()

@app.get("/")
async def read_root():
    try:
        logger.info("Root endpoint was called")
        return {"hello": "world"}
    except Exception as e:
        logger.exception("an error occurred in the root endpoint")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/item/{item_id}")
def read_item(item_id: int):
    try:
        logger.debug(f"item endpoint was called with item_id: {item_id}")
        return {"item_id": item_id}
    except Exception as e:
        logger.exception(f"an error occurred in the item endpoint for item_id: {item_id}")
        raise HTTPException(status_code=500, detail=str(e))


