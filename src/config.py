import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey")
    DEBUG = False
    TESTING = False
    # Add other base configuration variables here

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    # Add additional development-specific settings

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    # Add additional testing-specific settings

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Add additional production-specific settings

class SqlliteConfig(Config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')