# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/17 15:47'

from werkzeug.exceptions import HTTPException
from app import create_app
from app.help.error import APIException
from app.help.error_code import ServerError

app = create_app()

# AOP Flask 1.0
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1005
        return APIException(msg, code, error_code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e

if __name__ == '__main__':
    app.run(debug=True)
