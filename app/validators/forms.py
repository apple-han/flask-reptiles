# @Time    : 2019-06-01 08:01
# @Author  : __apple

from wtforms import StringField, IntegerField
from wtforms.validators import Length

from flask_wtf.file import FileField,FileRequired,FileAllowed

from app.validators.base import BaseForm as Form


class GoodsSearchForm(Form):
    q = StringField(validators=[Length(min=1, max=26)])
    collation = IntegerField(default=0)
    pageNo = IntegerField(default=1)


# class UploadForm(Form):
#     file = StringField(validators=[Length(min=1, max=26)])
