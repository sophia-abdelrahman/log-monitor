### Initializes the Flask app and bring together other components ###

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Import routes from the routes.py module
from app import routes