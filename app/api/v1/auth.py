# @Time    : 2020-01-08 20:01
# @Author  : __apple

from flask import jsonify, request, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.help.error_code import AuthFailed, Success
from app.help.redprint import Redprint
from app.validators.forms import LoginForm, RegisterForm
from base import log
from model.auth import User
from model.base import db

api = Redprint('auth')


@api.route('/login', methods=['POST'])
def login():
    form = LoginForm().validate_for_api()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not user.check_password(form.secret.data):
            log.logging.error('[ERROR] password or email is not Incorrect')
            raise AuthFailed()
        token = generate_token(user.id, current_app.config['EXPIRE'])
        t = {
            'token': token.decode('ascii')
        }
        return jsonify(t), 200


def generate_token(uid, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'uid': uid})


@api.route('/register', methods=['POST'])
def register():
    form = RegisterForm().validate_for_api()
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
    return Success()
