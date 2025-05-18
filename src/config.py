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
    UPLOAD_FOLDER = basedir + '/../app/input/'
    LOCAL_UPLOAD_FOLDER = basedir + '/../../envdev/apps_input/'  
    ALLOWED_EXTENSIONS = {'zip'}
    MAX_CONTENT_LENGTH = 16 * 1000 * 1000 #  16 MB limit

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