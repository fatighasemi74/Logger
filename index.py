import logging
from logging import StreamHandler, Formatter, LoggerAdapter
import os

logger = logging.getLogger("root")
consoleHandler = StreamHandler()
consoleHandler.setFormatter(Formatter("%(asctime)s - %(pid)s - %(org_name)s - %(levelname)s - %(message)s"))
logger.addHandler(consoleHandler)

loggerAdapter = LoggerAdapter(logger, extra={"org_name": "Name", "pid": os.getpid()})

loggerAdapter.warning("hello warning")
loggerAdapter.warning("hello2 warning")