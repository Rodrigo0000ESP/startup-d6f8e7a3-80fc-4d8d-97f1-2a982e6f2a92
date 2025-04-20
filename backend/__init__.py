import logging

# Initialize logging for the backend package
logging.basicConfig(level=logging.INFO)

# Import Flask app instance from app.py for package access
from .app import app

# Import and register blueprints from routes.py
from .routes import main_blueprint
app.register_blueprint(main_blueprint)