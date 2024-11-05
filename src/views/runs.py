from flask import Blueprint, render_template

runs = Blueprint("runs", __name__)

@runs.route("/")
def runs_list():
    return render_template("runs.html")