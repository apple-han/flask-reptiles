# @Time    : 2019-06-01 08:09
# @Author  : __apple

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.help.error_code import ServerError
from datetime import date


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder
