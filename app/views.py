"""
Define the routes and endpoints of the app
"""
from . import app # Import the Flask app instance from __init__.py


@app.route('/logs', methods=['GET'])
def get_logs():
    pass