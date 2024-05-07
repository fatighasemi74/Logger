import logging
from logging import LoggerAdapter

class AppLogger:
    __instance:LoggerAdapter = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AppLogger.__instance == None:
            AppLogger.initLogger()
        return AppLogger.__instance
    
    @staticmethod
    def initLogger():
        # get a named global logger
        appLogger = logging.getLogger("root")
        appLogger.setLevel(logging.INFO)

        # configure console logging
        streamHandler = logging.StreamHandler()
        fmt = "%(asctime)s - %(org_name)s - %(levelname)s - %(message)s"
        streamHandler.setFormatter(logging.Formatter(fmt))
        appLogger.addHandler(streamHandler)

        AppLogger.__instance = LoggerAdapter(appLogger, extra={"org_name": "org name"})