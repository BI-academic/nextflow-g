from utils import db
from datetime import datetime

# Model for the pipeline table
class Pipeline(db.Model):
    __tablename__ = 'pipeline'
    pipeline_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pipeline_name = db.Column(db.String(100), nullable=False)
    pipeline_version = db.Column(db.String(50), nullable=False)
    pipeline_description = db.Column(db.String(255), nullable=False)
    pipeline_file_path = db.Column(db.String(255), nullable=False)
    pipeline_main_nf = db.Column(db.String(255), nullable=False)
    
    # Relationship for easy access
    running_states = db.relationship('RunningState', backref='pipeline', lazy=True)
    profiles = db.relationship('Profile', backref='pipeline', lazy=True)

# Model for the running_state table
class RunningState(db.Model):
    __tablename__ = 'running_state'
    run_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pipeline_id = db.Column(db.Integer, db.ForeignKey('pipeline.pipeline_id'), nullable=False)
    resource_id = db.Column(db.Integer, nullable=False)  # Assuming resources model is defined elsewhere
    running_status = db.Column(db.String, nullable=False)
    working_directory = db.Column(db.String, nullable=False)

# Model for the users table
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Model for the profile table
class Profile(db.Model):
    __tablename__ = 'profile'
    profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    profile_name = db.Column(db.String, nullable=False)
    pipeline_id = db.Column(db.Integer, db.ForeignKey('pipeline.pipeline_id'), nullable=False)
    profile_executor = db.Column(db.String, nullable=False)
