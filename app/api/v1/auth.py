# @Time    : 2020-01-08 20:01
# @Author  : __apple

from flask import jsonify, request, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app import redis_client
from app.help.error_code import AuthFailed, Success, ParameterException
from app.help.redprint import Redprint
from app.help.email import send_mail
from app.validators.forms import LoginForm, RegisterForm, EmailForm
from base import log
from model.auth import User
from model.base import db
from util.generate_random import generate_code

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
        # 判断code是否正确
        key = "note:email:{}".format(form.email.data)
        if redis_client.get(key) and int(redis_client.get(key)) != form.code.data:
            raise ParameterException(msg='code码不正确,要重新获取喽', error_code=1012)
        with db.auto_commit():
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
    return Success()


@api.route('/email', methods=['POST'])
def email():
    form = EmailForm().validate_for_api()
    if request.method == 'POST' and form.validate():
        # 判断code是否在规定时间内已经发过
        key = "note:email:{}".format(form.email.data)
        value = redis_client.get(key)
        if value:
            raise ParameterException(msg='code 已经发过喽', error_code=1002)
        code = generate_code()
        send_mail(form.email.data, "注册开源项目", "register.html", name=form.email.data, code=code)
    return Success()
