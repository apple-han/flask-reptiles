# @Time    : 2019-06-01 08:01
# @Author  : __apple

from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import Length, DataRequired, Email, ValidationError, NumberRange

from app.validators.base import BaseForm as Form
from model.auth import User


class GoodsSearchForm(Form):
    q = StringField(validators=[Length(min=1, max=26)])
    collation = IntegerField(default=0)
    pageNo = IntegerField(default=1)


class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(6, 60), Email(message='邮箱格式不正确')])
    secret = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 36)])


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(6, 60), Email(message='邮箱格式不正确')])
    secret = PasswordField(validators=[DataRequired(message='密码不能为空'), Length(6, 36)])
    name = StringField(default="小花")
    code = IntegerField(validators=[DataRequired(message='code不能为空'), NumberRange(min=100000, max=999999)])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(6, 60), Email(message='邮箱格式不正确')])
