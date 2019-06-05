# @Time    : 2019-06-03 20:13
# @Author  : __apple

from app.help.error_code import NotFound

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import inspect, Column, Integer, SmallInteger, orm
from contextlib import contextmanager


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete(self):
        self.status = 0

    def keys(self):
        return self.fields

    def hide(self, *keys):
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            self.fields.append(key)
        return self

class cached_property(object):
    def __init__(self, func, name=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.func = func

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, None)
        if value is None:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value

class Pagination(object):
    def __init__(self, query, page, per_page=15, need_total=True):
        self.query = query
        self.per_page = per_page if per_page > 0 else 20
        self.need_total = need_total
        self.page = page
        if page < 1: page = 1


    @cached_property
    def total(self):
        if self.need_total:
            return self.query.count()
        # 伪分页
        if len(self.items) > 0:
            return self.page * self.per_page + 200
        else:
            return self.page * self.per_page

    @cached_property
    def items(self):
        return self.query.offset((self.page - 1) * self.per_page).limit(self.per_page).all()

    def iter_pages(self, left_edge=1, left_current=1,
                   right_current=2, right_edge=1):
        if not self.need_total:
            yield None
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
                    (num > self.page - left_current - 1 and \
                     num < self.page + right_current) or \
                    num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num

    @cached_property
    def has_prev(self):
        return self.page > 1

    @cached_property
    def prev_num(self):
        return self.page - 1

    @cached_property
    def has_next(self):
        if self.total:
            return self.page < self.pages
        else:
            return self.per_page == len(self.items)

    @cached_property
    def next_num(self):
        return self.page + 1

    @cached_property
    def pages(self):
        if self.total:
            return max(0, self.total - 1) // self.per_page + 1



class MixinJSONSerializer:
    @orm.reconstructor
    def init_on_load(self):
        self._fields = []
        # self._include = []
        self._exclude = []

        self._set_fields()
        self.__prune_fields()

    def _set_fields(self):
        pass

    def __prune_fields(self):
        columns = inspect(self.__class__).columns
        if not self._fields:
            all_columns = set(columns.keys())
            self._fields = list(all_columns - set(self._exclude))

    def hide(self, *args):
        for key in args:
            self._fields.remove(key)
        return self

    def keys(self):
        return self._fields

    def __getitem__(self, key):
        return getattr(self, key)
