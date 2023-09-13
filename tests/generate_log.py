import os
import random
import argparse
from config import configure_logger, LOG_FILE_NAME, LOG_FILE_SIZE_GB
from datetime import datetime


logger = configure_logger()


def generate_log(log_file_path, size_gb):
    logger.debug("Generating test log file...")
    log_levels = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sample_log = f"{current_time} - Line 1: INFO - This is a sample log line for our file.\n"
    lines_needed = int((size_gb * (10 ** 9)) / len(sample_log))

    with open(log_file_path, 'w') as f:
        for line_number in range(1, lines_needed + 1):
            log_level = random.choice(log_levels)
            log_line = f"{current_time} - Line {line_number}: {log_level} - This is a sample log line for our file.\n"
            f.write(log_line)

        f.write('A' * (int(size_gb * 10 ** 9) - f.tell()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a test log file.")
    parser.add_argument("--name", default=LOG_FILE_NAME, help="Name of the log file.")
    parser.add_argument("--size", default=LOG_FILE_SIZE_GB, type=float, help="Size of the log file in GB.")

    args = parser.parse_args()

    log_file_path = os.path.join(os.getcwd(), args.name)

    generate_log(log_file_path, args.size)

    logger.debug(f"Test log file created at {log_file_path}")