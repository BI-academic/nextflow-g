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

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/nextflow_g.db')

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
    # Add additional testing-specific settings

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/nextflow_g.db')

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Add additional production-specific settings

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/nextflow_g.db')