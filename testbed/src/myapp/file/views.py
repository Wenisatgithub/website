#!/usr/bin/python
# coding:utf-8

import os
from flask import request, render_template, send_from_directory, redirect, url_for, Blueprint
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from wtforms import SubmitField
from myapp.user.user import user_directory

file_bp  = Blueprint('file',__name__, template_folder='templates')

@file_bp.route('/file_mgmt', methods=['GET'])
def file_mgmt():
    path_lists = []
    user_dir = user_directory()
    for lst in os.walk( user_dir.get() ):
        path_dicts = {'root': '', 'dirs': '', 'files': ''}
        path_dicts['root'] = lst[0].replace( user_dir.get() , '/')
        path_dicts['dirs'] = lst[1]
        path_dicts['files'] = lst[2]
        path_lists.append(path_dicts)

    filename_lists = []
    for path in path_lists:
        for file in path['files']:
            filename_lists.append(os.path.join(path['root'], file))

    file_lists = []
    for filename in filename_lists:
        file_dicts = {'filename': '', 'filefullname': ''}
        file_dicts['filename'] = os.path.split(filename)[1]
        file_dicts['filefullname'] = filename
        file_lists.append(file_dicts)

    return render_template('file/file_mgmt.html', file_lists=file_lists)

@file_bp.route('/download/<path:filename>', methods=['GET'])
def file_download(filename):
    user_dir = user_directory()
    return send_from_directory( user_dir.get(), filename, as_attachment=True)

@file_bp.route('/rename/<path:filename>', methods=['POST'])
def file_rename(filename):
    user_dir = user_directory()
    originfile = user_dir.get() + filename
    originfilepath = os.path.split(originfile)[0] + '/'
    newfile = originfilepath + request.form['newname']
    os.rename(originfile, newfile)
    return redirect(url_for('file.file_mgmt'))

@file_bp.route('/delete/<path:filename>', methods=['GET'])
def file_delete(filename):
    user_dir = user_directory()
    originfile = user_dir.get() + filename
    os.remove(originfile)
    return redirect(url_for('file.file_mgmt'))

###########################################################################################
# user_dir = user_directory()
# file.config['UPLOADED_PHOTOS_DEST'] = user_dir.get()
# photos = UploadSet('photos', IMAGES)
# configure_uploads(file, photos)
# patch_request_class(file)
#
# class UploadForm(FlaskForm):
#     photo = FileField(validators=[
#         FileAllowed(['jpg','png'], u'只能上传图片！'),
#         FileRequired(u'文件未选择！')])
#     submit = SubmitField(u'上传')
#
@file_bp.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'GET':
        fileName = None
    else:
        fileObj = request.files['uploadFileName']
        fileName = fileObj.filename
        user_dir = user_directory()
        fileDir = user_dir.get()
        if fileName:
            fileObj.save(fileDir + str(fileName))
    return render_template('file/file_upload.html', filename=fileName)

    # form = UploadForm()
    # if form.validate_on_submit():
    #     filename = photos.save(form.photo.data)
    #     file_url = photos.url(filename)
    # else:
    #     file_url = None
    # return render_template('file/file_upload.html', form=form, file_url=file_url)