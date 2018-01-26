# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/17 15:47'

import sys
sys.path.append('/data/love_spider')
from flask import Flask
from flask.ext.restful import Api

from api.commodity.search import SearchAPI

app = Flask(__name__)
api = Api(app)


api.add_resource(SearchAPI, '/search/api/')

if __name__ == '__main__':
    app.run(debug=True)
