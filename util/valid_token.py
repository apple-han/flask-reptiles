from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.help.error_code import AuthFailed

auth = HTTPTokenAuth(scheme='Token')
User = namedtuple('User', ['uid'])


@auth.verify_token
def verify_token(token):
    print(token)
    info = verify_token(token)
    if not info:
        return False
    else:
        g.user = info
        return True


def verify_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid')
    except SignatureExpired:
        raise AuthFailed(msg='token is expired')
    uid = data['uid']
    return User(uid)