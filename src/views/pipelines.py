from flask import Blueprint, render_template

pipelines = Blueprint("pipelines", __name__)

@pipelines.route("/")
def pipelines_list():
    return render_template("pipelines.html")

@pipelines.route("/install")
def pipeline_install():
    return render_template("pipeline_install.html")