from functools import wraps
from flask import session, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Custom decorator to require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to be logged in to access this page.', 'danger')
            return redirect(url_for('auth.login'))  # Change 'auth.login' to your login route if needed
        return f(*args, **kwargs)
    return decorated_function