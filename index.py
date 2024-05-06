import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

fileHandler = RotatingFileHandler("test.log", maxBytes=1024, backupCount=100)
fileFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
fileHandler.setFormatter(fileFormatter)

logger.addHandler(fileHandler)

logger.info("info log")
logger.warning("this is warning log")

try:
    x = 1/0
except Exception as e:
    logger.error("some error occured", exc_info=e)