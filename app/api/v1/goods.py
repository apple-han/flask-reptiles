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



# class AssociateApi(Resource,BaseHandler):
#     def __init__(self):
#         super().__init__()
#     def get(self):
#         associate_key = request.args.get("associate_key")
#         associate_key = associate_key.replace(' ', '')
#         if associate_key:
#             result = SearchAPI().split_name(associate_key)
#             if result:
#                 for r in result:
#                     codes = chinese_to_number(r)
#                     if codes[0]:
#                         files = splicing_path(codes[1])
#                         listdirs = os.listdir(files.get('folder_path'))
#                         folder_path = files.get('folder_path')
#                         dict_associate = Counter()
#                         for listdir in listdirs:
#                             file_path_associate = folder_path+os.sep+listdir+os.sep+'search.big'
#                             result_associate = os_path.read_file_to_search(file_path_associate)
#                             if result_associate:
#                                 result_len = len(result_associate)
#                                 dict_associate[listdir] = result_len
#                         dict_bank = dict_associate.most_common(5)
#                         dict_result_bank = dict()
#                         dict_result_bank['first'] = associate_key+chr(int(dict_bank[0][0]))
#                         dict_result_bank['second'] = associate_key+chr(int(dict_bank[1][0]))
#                         dict_result_bank['third'] = associate_key+chr(int(dict_bank[2][0]))
#                         dict_result_bank['forth'] = associate_key+chr(int(dict_bank[3][0]))
#                         dict_result_bank['fifth'] = associate_key+chr(int(dict_bank[4][0]))
#
#                         self.success['bank'] = dict_result_bank
#                         return json.dumps(self.success, cls=CommodityEncoder)



