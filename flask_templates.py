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
    "models/db.py": (
        "# Database models for the Flask app.\n"
        "from flask_sqlalchemy import SQLAlchemy\n\n"
        "db = SQLAlchemy()\n\n"
        "# Define your data models here\n"
    ),
    "routes/abc.py": (
        "# Route definitions for the Flask app.\n"
        "from . import app\n"
        "from flask import jsonify, request\n\n"
        "# Define your Flask routes here\n"
        "@app.route('/')\n"
        "def home():\n"
        "    return jsonify(message='Welcome to the Flask app!')\n"
    ),
    "schemas/abcd.py": (
        "# Marshmallow schemas for the Flask app.\n"
        "from marshmallow import Schema, fields\n\n"
        "# Define your schemas here\n"
    ),
    "utils/abcde.py": (
        "# Utility functions for the Flask app.\n"
        "# Define your utility functions here\n"
    ),
    "config.py": (
        "# Configuration settings for the Flask app.\n"
        "class Config:\n"
        "    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')\n"
        "    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')\n"
        "    SQLALCHEMY_TRACK_MODIFICATIONS = False\n"
        "    # Additional configuration parameters here\n"
    ),
    "main.py": (
        "# The main entry point for starting the Flask app.\n"
        "from app import app\n\n"
        "if __name__ == '__main__':\n"
        "    app.run(debug=True)\n"
    ),
    "__init__.py": "",
    "tests/test_app.py": (
        "# Basic tests for the Flask app.\n"
        "import unittest\n"
        "from app import app\n\n"
        "class BasicTests(unittest.TestCase):\n"
        "    def setUp(self):\n"
        "        app.config['TESTING'] = True\n"
        "        self.app = app.test_client()\n"
        "        self.app_context = app.app_context()\n"
        "        self.app_context.push()\n\n"
        "    def tearDown(self):\n"
        "        self.app_context.pop()\n\n"
        "    def test_home(self):\n"
        "        response = self.app.get('/')\n"
        "        self.assertEqual(response.status_code, 200)\n"
        "        self.assertIn('Welcome to the Flask app!', response.get_data(as_text=True))\n\n"
        "if __name__ == '__main__':\n"
        "    unittest.main()\n"
    )
}