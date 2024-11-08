from flask import Blueprint, render_template

pipelines = Blueprint("pipelines", __name__)

@pipelines.route("/")
def pipelines_list():
    return render_template("pipelines.html")