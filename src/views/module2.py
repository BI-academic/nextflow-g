from flask import Blueprint, render_template

second_blueprint = Blueprint("second_blueprint", __name__)

@second_blueprint.route("/")
def second_home():
    return render_template("second_home.html")

@second_blueprint.route("/hello")
def second_hello():
    return render_template("second_hello.html")