"""MODULE"""
import os
<<<<<<< HEAD
from flask import Flask
from route import v1
def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    if os.environ.get('FLASK_ENV') == 'development':
        # app.logger.info(os.environ.get('FLASK_ENV'))
        app.config.from_object('config.Development')
        print("Development")
    elif os.environ.get('FLASK_ENV') == 'testing':
        # app.logger.info(os.environ.get('FLASK_ENV'))
        app.config.from_object('config.Testing')
        print("Testing")
    else:
        # app.logger.info(os.environ.get('FLASK_ENV'))
        app.config.from_object('config.Production')
        print("Production")

    with app.app_context():
        # Import parts of our application
        # Register Blueprints
        app.register_blueprint(v1)
        return app