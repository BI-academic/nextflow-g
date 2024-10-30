# app.py
import os
from flask import Flask
from views.module1 import first_blueprint
from views.module2 import second_blueprint
from config import DevelopmentConfig, TestingConfig, ProductionConfig

def create_app():
    app = Flask(__name__)

    # Choose configuration based on environment variable, or use DevelopmentConfig by default
    env = os.environ.get("FLASK_ENV", "development")

    if env == "production":
        app.config.from_object(ProductionConfig)
    elif env == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    # Register the blueprints
    app.register_blueprint(first_blueprint, url_prefix="/first")
    app.register_blueprint(second_blueprint, url_prefix="/second")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)