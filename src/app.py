# app.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_wtf import CSRFProtect
from utils import db

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


    # DB setting
    db.init_app(app)
    
    # Initialize CSRF protection
    csrf = CSRFProtect(app)

    # DB setting
    from models import Pipeline, RunningState, User, Profile

    # Blueprint setting
    from views.home import landing
    from views.pipelines import pipelines
    from views.runs import runs
    from views.login import auth_bp

    # Register the blueprints
    app.register_blueprint(landing, url_prefix="/")
    app.register_blueprint(pipelines, url_prefix="/pipelines")
    app.register_blueprint(runs, url_prefix="/runs")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    with app.app_context():
        db.create_all()


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)