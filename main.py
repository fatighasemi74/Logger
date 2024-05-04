from fastapi import FastAPI
from logger import logger

app = FastAPI()
logger.info('starting app........')

@app.get("/")
async def index() -> dict:
    logger.info('request to indext page')
    return {'message': 'hello'}

@app.get("/upload-videos")
async def index() -> dict:
    logger.info('request to upload videos')
    return {'message': 'upload videos'}