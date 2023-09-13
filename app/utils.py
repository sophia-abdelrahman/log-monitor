"""
Utility functions, i.e., reading and filtering log files
"""
import os
import io
import logging
from config import LOG_DIR

def retrieve_logs(filename, keyword=None, last_n=10):
    log_path = os.path.join(LOG_DIR, filename)

    if not os.path.exists(log_path):
        return None, f"No such file: {log_path}"

    # Read the file, filter the lines, and return them
    with io.open(log_path, 'r', encoding='utf-8', errors='ignore') as log_file:
        lines = log_file.readlines()

        # If specified, filter lines by keyword
        if keyword:
            lines = [line for line in lines if keyword in line]

        # Get the last n lines, in reverse order (newest first)
        lines = lines[-last_n:][::-1]

    return lines, None

