

templates = {
    "app/__init__.py": (
        "# Main module for the Flask application.\n"
        "from flask import Flask\n"
        "from .config import Config\n\n"
        "app = Flask(__name__)\n"
        "app.config.from_object(Config)\n\n"
        "# Import modules here\n"
        "from .models import db\n"
        "from .routes import *\n"
        "from .schemas import *\n"
        "from .utils import *\n\n"
        "db.init_app(app)\n"
    ),
    "db.py": (
        "# Database models for the Flask app.\n"
        "from . import db\n\n"
        "# Define your data models here\n"
    ),
    "abc.py": (
        "# Route definitions for the Flask app.\n"
        "from . import app\n"
        "from flask import jsonify, request\n\n"
        "# Define your Flask routes here\n"
    ),
    "abcd.py": (
        "# Marshmallow schemas for the Flask app.\n"
        "from marshmallow import Schema, fields\n\n"
        "# Define your schemas here\n"
    ),
    "abcde.py": (
        "# Utility functions for the Flask app.\n"
        "# Define your utility functions here\n"
    ),
    "config.py": (
        "# Configuration settings for the Flask app.\n"
        "class Config:\n"
        "    SECRET_KEY = 'your_secret_key_here'\n"
        "    SQLALCHEMY_DATABASE_URI = 'database_url_here'\n"
        "    # Additional configuration parameters here\n"
    ),
    "main.py": (
        "# The main entry point for starting the Flask app.\n"
        "from app import app\n\n"
        "if __name__ == '__main__':\n"
        "    app.run(debug=True)\n"
    ),
    "__init__.py": "" 
}