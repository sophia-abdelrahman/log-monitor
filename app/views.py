"""
Define the routes and endpoints of the app
"""
import logging
from flask import render_template, request, jsonify, redirect
from .utils import retrieve_logs
from . import app
from config import LOG_DIR, LOG_FILE_NAME
from .errors import FileNameError, KeywordError, LastNError


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Bind the 'get_logs()' view function/endpoint to the '/logs' route for GET requests
@app.route('/logs', methods=['GET'])
def get_logs():
    """
    Endpoint to get log lines based on the following query parameters:

    - filename: Name of the log file to retrieve.
    - keyword: Keyword to filter log lines (optional).
    - last_n: Number of most recent log lines to retrieve (default is 10).

    Returns:
        JSON response containing log lines or an error message.
    """
    params = {
        "filename": request.args.get('filename', LOG_FILE_NAME),
        "keyword": request.args.get('keyword', None),
        "last_n": request.args.get('last_n', 10) # Default to 10 if not specified
    }

    error_response, error_code = validate_parameters(params)
    if error_response:
        return error_response, error_code

    exception_to_error = {
        FileNameError: ("Invalid filename provided.", 400),
        KeywordError: ("Invalid keyword provided.", 400),
        LastNError: ("Invalid value for last_n provided.", 400),
    }

    try:
        # Use the utility function to retrieve and filter logs
        lines, error = retrieve_logs(params['filename'], params['keyword'], int(params['last_n']))
        if error:
            return jsonify({"error": error}), 404
        return render_template("index.html", logs='\n'.join(lines))
    except tuple(exception_to_error.keys()) as caught_exception:
        error_msg, status_code = exception_to_error[type(caught_exception)]
        return jsonify({"error": error_msg}), status_code
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500


@app.route('/')
def index():
    return "Welcome to the log-monitor API!"


VALIDATORS = {
    'filename': {
        'condition': lambda x: x and isinstance(x, str) and '..' not in x and 0 < len(x) <= 255,
        'error': "Invalid filename. Ensure it's a string between 1-255 characters without '..'."
    },
    'keyword': {
        'condition': lambda x: not x or (isinstance(x, str) and 0 < len(x) <= 100 and x.strip()),
        'error': "Invalid keyword. Ensure it's a string between 1-100 characters."
    },
    'last_n': {
        'condition': lambda x: (x == 10 or (isinstance(x, str) and x.isdigit() and int(x) > 0)),
        'error': "last_n should be a positive integer."
    }
}


def validate_parameters(params):
    for param, value in params.items():
        # Attempt to retrieve the validator for the parameter. If not found, use an empty dictionary.
        validator = VALIDATORS.get(param, {})
        condition = validator.get('condition')
        error = validator.get('error')

        if condition and not condition(value):
            return jsonify({"error": error}), 400
    return None, None

