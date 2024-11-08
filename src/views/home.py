from flask import Blueprint, render_template
from utils import login_required


landing = Blueprint("landing", __name__)

@landing.route("/")
@login_required
def home():
    return render_template("home.html")