from flask import Blueprint, render_template, flash, request, redirect, url_for, send_from_directory, current_app
from werkzeug.utils import secure_filename
from models import Pipeline
from app import db
import os 
from pathlib import Path
import zipfile
from config import DevelopmentConfig

pipelines = Blueprint("pipelines", __name__)

local = False
UPLOAD_FOLDER = DevelopmentConfig.LOCAL_UPLOAD_FOLDER if local else DevelopmentConfig.UPLOAD_FOLDER
ALLOWED_EXTENSIONS = DevelopmentConfig.ALLOWED_EXTENSIONS
print('UPLOAD_FOLDER:', UPLOAD_FOLDER)

@pipelines.route("/")
def pipelines_list():
    return render_template("pipelines.html")

@pipelines.route('/install', methods=['GET', 'POST'])
def pipeline_install():
    if request.method == 'POST':
        # 폼 데이터 가져오기
        pipeline_name = request.form['pipeline_name']
        pipeline_version = request.form['pipeline_version']
        pipeline_description = request.form['pipeline_description']
        pipeline_main_nf = request.form['pipeline_main_nf']
        file = request.files['pipeline_file']

        # .zip 파일 압축 해제 폴더
        pipeline_dir = os.path.join(UPLOAD_FOLDER, pipeline_name)
        
        # .zip 파일이 올바른지 확인
        if file and file.filename.endswith('.zip'):
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            # 파일을 서버에 저장
            file.save(file_path)

            pipeline_file_path = os.path.join(pipeline_dir, file.filename)

            # Pipeline 정보 DB에 저장
            new_pipeline = Pipeline(
                pipeline_name=pipeline_name,
                pipeline_version=pipeline_version,
                pipeline_description=pipeline_description,
                pipeline_file_path=pipeline_file_path,
                pipeline_main_nf = pipeline_main_nf
            )
            db.session.add(new_pipeline)
            db.session.commit()
            
            # 폴더가 없다면 생성
            if not os.path.exists(pipeline_dir):
                os.makedirs(pipeline_dir)

            try:
                # 압축 해제
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(pipeline_dir)                  
                flash(f'Pipeline {pipeline_name} version {pipeline_version}, unzip dir {pipeline_file_path} installed and saved to the database!', 'success')
                return redirect(url_for('pipelines.pipelines_list' ))
            except zipfile.BadZipFile:
                return 'Invalid zip file format', 400
        else:
            return 'Please upload a valid .zip file.', 400

    return render_template("pipeline_install.html")