"""
Define the routes and endpoints of the app
"""
from flask import request, jsonify # Import necessary modules and functions from Flask
from .utils import retrieve_logs # Import utility function to retrieve logs from local modules
from . import app # Import the Flask app instance from __init__.py
from config import LOG_DIR, DEFAULT_LAST_N # Import configuration settings


# Bind the 'get_logs()' view function/endpoint to the '/logs' route for GET requests
@app.route('/logs', methods=['GET'])
def get_logs():
    filename = request.args.get('filename', None)
    keyword = request.args.get('keyword', None)
    last_n = int(request.args.get('last_n', DEFAULT_LAST_N))

    if not filename:
        return jsonify({"error": "filename is required as a query parameter"}), 400

    # Use the utility function to retrieve and filter logs
    lines, error = retrieve_logs(filename, keyword, last_n)

    # Handle errors from the log retrieval TODO: MAKE more robust
    if error:
        return jsonify({"error": error}), 404

    return jsonify({"lines": lines})