# @Time    : 2020-01-08 20:11
# @Author  : __apple
from enum import IntEnum

from flask import current_app
from sqlalchemy import Column, Integer, String, orm, func
from werkzeug.security import check_password_hash, generate_password_hash

from model.base import Base, Pagination, db


class Volume(IntEnum):
    IDS = 0  # ids 排序
    PRICE = 1  # 价格


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False)
    _secret = Column('secret', String(128), nullable=False)
    name = Column(String(24), nullable=True)

    def check_password(self, key):
        return check_password_hash(self._secret, key)

    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, key):
        self._secret = generate_password_hash(key)

