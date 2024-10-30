from flask import Blueprint, render_template

first_blueprint = Blueprint("first_blueprint", __name__)

@first_blueprint.route("/")
def first_home():
    return render_template("first_home.html")

@first_blueprint.route("/hello")
def first_hello():
    return render_template("first_hello.html")