import os
import random
import argparse
from config import configure_logger, LOG_FILE_NAME, LOG_FILE_SIZE_GB

logger = configure_logger()

def generate_log(log_file_path, size_gb):
    logger.debug("Generating test log file...")
    log_levels = ['INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL']

    sample_log = f"Line 1: INFO - This is a sample log line for our file.\n"
    lines_needed = int((size_gb * (10 ** 9)) / len(sample_log))

    with open(log_file_path, 'w') as f:
        for line_number in range(1, lines_needed + 1):
            log_level = random.choice(log_levels)
            log_line = f"Line {line_number}: {log_level} - This is a sample log line for our file.\n"
            f.write(log_line)

        f.write('A' * (int(size_gb * 10 ** 9) - f.tell()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a test log file of specified size.")
    parser.add_argument("--name", default=LOG_FILE_NAME, help="Name of the log file to be generated or overwritten.")
    parser.add_argument("--size", default=LOG_FILE_SIZE_GB, type=float, help="Desired size of the log file in GB.")

    args = parser.parse_args()

    log_file_path = os.path.join(os.getcwd(), args.name)

    if os.path.exists(log_file_path):
        logger.warning(f"Log file {log_file_path} already exists and will be overwritten!")

    generate_log(log_file_path, args.size)

    logger.debug(f"Test log file created at {log_file_path}")