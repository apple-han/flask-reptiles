# @Time    : 2019-06-01 08:01
# @Author  : __apple

import os

from flask import jsonify, url_for, request, send_from_directory, redirect

from app.help.error_code import UploadException
from app.help.redprint import Redprint
from werkzeug.utils import secure_filename
from config.config import UPLOAD_PATH
from util import upload as u

api = Redprint('file')


@api.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_PATH, filename)


@api.route("/upload", methods=['POST'])
def upload():
    # 获取参数
    f = request.files.get('image')
    if not f or not u.allowed_file(f.filename):
        raise UploadException()
    filename = secure_filename(f.filename)
    m = filename.rsplit('.', 1)[1]
    f_name = u.create_uuid() + "." + m
    f.save(os.path.join(UPLOAD_PATH, f_name))
    r = dict(code=0, url=url_for('v1.file+uploaded_file', filename=f_name, _external=True))
    return jsonify(r)

