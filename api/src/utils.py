import os
import logging
from logging.handlers import RotatingFileHandler

import config

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def get_logger(name, path, level=logging.INFO, size=1024*1024*5, backups=5):
    if not os.path.exists(config.logs_path):
        os.makedirs(config.logs_path)
        
    handler = RotatingFileHandler(path, maxBytes=size, backupCount=backups, encoding='utf-8')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
