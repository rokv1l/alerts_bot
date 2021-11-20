import logging
from os import getenv
from logging.handlers import RotatingFileHandler

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logs_path = getenv('LOGS_PATH')


def get_logger(name, path, level=logging.INFO, size=1024*1024*5, backups=5):
    handler = RotatingFileHandler(path, maxBytes=size, backupCount=backups, encoding='utf-8')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
