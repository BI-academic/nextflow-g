from flask import Blueprint, render_template, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from config import PipelinesConfig
import os

pipelines = Blueprint("pipelines", __name__)

ALLOWED_EXTENSIONS = PipelinesConfig.ALLOWED_EXTENSIONS
UPLOAD_FOLDER = PipelinesConfig.UPLOAD_FOLDER

@pipelines.route("/")
def pipelines_list():
    return render_template("pipelines.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@pipelines.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_FOLDER, name)

@pipelines.route('/install', methods=['GET', 'POST'])
def pipeline_install():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(PipelinesConfig.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('unzip_local', name=filename))

    return render_template("pipeline_install.html")