# -*- coding: utf-8 -*-
__author__ = '__apple'
__time__ = '2018/1/17 15:47'

from flask import Flask
from flask.ext.restful import Api

from api.commodity.search import SearchAPI

app = Flask(__name__)
api_fast = Api(app)


api_fast.add_resource(SearchAPI, '/search/api/')

if __name__ == '__main__':
    app.run(debug=True)