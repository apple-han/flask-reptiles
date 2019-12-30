# @Time    : 2019-06-01 08:01
# @Author  : __apple

from flask import Blueprint
from app.api.v1 import goods, file


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    goods.api.register(bp_v1)
    file.api.register(bp_v1)
    return bp_v1
