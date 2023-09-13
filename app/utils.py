"""
Utility functions, i.e., reading and filtering log files
"""
import os
import io
import logging
from config import LOG_DIR
from .errors import FileNameError, KeywordError, LastNError

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def retrieve_logs(filename, keyword=None, last_n=10):
    """
    Retrieve the last n lines from a log file, optionally filtered by a keyword.

    Args:
    - filename (str): The name of the log file.
    - keyword (str, optional): A keyword to filter the lines. Defaults to None.
    - last_n (int, optional): Number of lines to retrieve. Defaults to 10.

    Returns:
    - tuple: A tuple containing the list of lines and an error message or None.
    """
    log_path = os.path.join(LOG_DIR, filename)

    # Use helper functions for file and parameter validations
    file_exists(log_path)
    validate_filename(filename)
    validate_keyword(keyword)
    validate_last_n(last_n)

    with open(log_path, 'rb') as f:
        f.seek(0, os.SEEK_END)
        position, chunk_size, data, lines = f.tell(), 4096, b"", []

        while position > 0 and len(lines) < last_n:
            position = max(position - chunk_size, 0)
            f.seek(position)
            data = f.read(chunk_size) + data
            lines = data.splitlines()

        if keyword:
            lines = [line for line in lines if keyword.encode() in line]

    return [line.decode('utf-8') for line in lines[-last_n:]][::-1], None


def validate_filename(filename):
    if not isinstance(filename, str) or '..' in filename or not 0 < len(filename) <= 255:
        raise FileNameError("Filename should be a valid string (1-255 characters) without '..'.")


def validate_last_n(last_n):
    if not isinstance(last_n, int) or last_n <= 0:
        raise LastNError("last_n should be a positive integer.")


def validate_keyword(keyword):
    if keyword and (not isinstance(keyword, str) or not 0 < len(keyword.strip()) <= 100):
        raise KeywordError("Keyword should be a valid string (1-100 characters).")


def file_exists(log_path):
    if not os.path.exists(log_path):
        raise FileNameError(f"No such file: {log_path}")