# @Time    : 2019-06-01 08:01
# @Author  : __apple

import json
import os

from flask import jsonify
from app.help.redprint import Redprint
from app.validators.forms import GoodsSearchForm
from model.goods import Goods
from util.search import split_name, require_ids

api = Redprint('goods')


@api.route("/search")
def search():
    # 验证参数
    form = GoodsSearchForm().validate_for_api()
    # 获取参数
    q = form.q.data
    pageNo = form.pageNo.data
    collation = form.collation.data

    # 拆分关键字
    result = split_name(q)
    # 获取id
    ids = require_ids(result)
    # 查询数据返回对象
    pg = Goods.find_commoditys_by_ids(ids, int(pageNo), collation)

    r = dict(code=0, result=dict(
        items=[i for i in pg.items],
        total=pg.total,
        has_next=pg.has_next))
    return jsonify(r)
