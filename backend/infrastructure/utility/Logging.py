# python standard library
from logging import getLogger, Formatter, StreamHandler, FileHandler, DEBUG, INFO
from datetime import datetime, timedelta, timezone


class Logging:

    tz = timezone(timedelta(hours=+9), 'Asia/Tokyo')
    now = datetime.now(tz)
    LOG_FILE = './logs/python_' + now.date().strftime('%Y%m%d') + '.log'
    loggers = {}

    @classmethod
    def get(cls, *, module):

        if cls.loggers.get(module):
            return cls.loggers.get(module)

        logger = getLogger(module)

        logger = cls.set(logger, StreamHandler(), True)
        logger = cls.set(logger, FileHandler(cls.LOG_FILE), True)

        logger.setLevel(DEBUG)
        logger.propagate = False

        cls.loggers[module] = logger
        return logger


    @staticmethod
    def set(logger, handler, debug_mode):
        if debug_mode:
            handler.setLevel(DEBUG)
        else:
            handler.setLevel(INFO)

        handler.setFormatter(Formatter('%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s'))

        logger.addHandler(handler)
        return logger