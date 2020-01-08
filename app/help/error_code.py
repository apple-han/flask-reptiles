# @Time    : 2019-06-03 20:06
# @Author  : __apple
from app.help.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class UploadException(APIException):
    code = 400
    msg = 'upload image fail please try again!'
    error_code = 1007


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, sorry'


class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorization failed'
