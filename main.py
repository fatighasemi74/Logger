import json
import logging
import logging.config
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# load logging configuration
with open('logging_config.json', 'r') as config_file:
    logging_config = json.load(config_file)
logging.config.dictConfig(logging_config)

# create logger
logger = logging.getLogger("my_app")

app = FastAPI()

# This will act as our fake database for now
fake_db = {}

# Pydantic model to represent our data structure
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    on_offer: bool = False




@app.get("/")
async def read_root():
    try:
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")
        return {"hello": "world"}
    except Exception as e:
        logger.exception("an error occurred in the root endpoint")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/change_logging_level/{level}")
async def change_logging_level(level: str):
    if level.upper() in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
        logger.setLevel(level.upper())
        return {"message": f"Logging level set to {level.upper()}"}
    else:
        return {"message": "Invalid logging level provided. Valid levels are DEBUG, INFO, WARNING, ERROR, CRITICAL"}

@app.post("/item/{item_id}", response_model=Item)
async def create_item(item_id: int, item:Item):
    try:
        if item_id in fake_db:
            logger.info(f"item exists")
            raise HTTPException(status_code=400, detail="Item exists.")
        fake_db[item_id] = item
        logger.info(f"created item with id: {item_id}")
        return fake_db[item_id]
    except HTTPException as http_exc:
        logger.error(f"http error: {http_exc.detail}")
        raise
    except Exception as exc:
        logger.exception(f"an error occurred: {exc}")
        raise HTTPException(status_code=500, detail="an unexpected error")

@app.get("/item/{item_id}", response_model=Item)
async def read_item(item_id: int):
    try:
        if item_id not in fake_db:
            raise HTTPException(status_code=404, detail="item not found.")
        logger.info(f"Retrieved item with id: {item_id}", extra={"request_id": "some_unique_identifier"})
        return fake_db[item_id]
    except HTTPException as http_exc:
        logger.error(f"an http error occurred: {http_exc.detail}")
        raise
    except Exception as exc:
        logger.exception(f"an unexpected error: {exc}")
        raise HTTPException(status_code=500, detail="an unexpected error")



