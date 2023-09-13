import logging
import os

LOG_DIR = os.path.join(os.getcwd())
LOG_FILE_NAME = 'sample.log'
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)
LOG_FILE_SIZE_GB = 0.001

def configure_logger():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    return logger

