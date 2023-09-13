import os
import random
from config import LOG_FILE_SIZE_GB, LOG_FILE_PATH, LOG_FILE_NAME, configure_logger

logger = configure_logger()

def generate_log():
    logger.debug("Generating test log file...")
    log_levels = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']
    with open(LOG_FILE_PATH, 'w') as f:
        for line_number in range(1, lines_needed + 1):
            log_level = random.choice(log_levels)
            log_line = f"Line {line_number}: {log_level} - This is a sample log line for our file.\n"
            f.write(log_line)

        f.write('A' * (int(LOG_FILE_SIZE_GB * 10 ** 9) - f.tell()))

lines_needed = int((LOG_FILE_SIZE_GB * (10 ** 9)) / len("Line 1: INFO - This is a sample log line for our file.\n"))

generate_log()

print(f"Test log file created at {LOG_FILE_PATH}")