"""
Initialize the Flask app
"""
from flask import Flask

app = Flask(__name__) # Create a Flask app instance

from app import views # Import routes from the views.py module (register the routes with the Flask app instance)