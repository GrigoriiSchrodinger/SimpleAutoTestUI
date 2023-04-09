import logging
from logging import Logger


def setup_custom_logger(name) -> Logger:
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    return logger
