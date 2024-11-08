from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from models import User
from app import db

auth_bp = Blueprint('auth', __name__)

# Route to the home page
@auth_bp.route('/')
def home():
    return render_template('login.html')

# Route for the registration page
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        current_app.logger.info(f"existed user: {existing_user.username}")

        if existing_user:
            flash('Username already exists. Please choose another one.', 'danger')
            return redirect(url_for('auth.register'))

        # Hash the password and create a new user
        hashed_password = generate_password_hash(password, method='scrypt')
        new_user = User( username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

# Route for the login page
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists
        user = User.query.filter_by(username=username).first()
        if user:
            current_app.logger.info(f"Login user email: {user.email}")

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.username
            flash('Logged in successfully!', 'success')
            return redirect(url_for('landing.home'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')

# Route for logging out
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.home'))