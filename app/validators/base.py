# @Time    : 2019-06-03 20:06
# @Author  : __apple
from flask import request
from wtforms import Form

from app.help.error_code import ParameterException



class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()

        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self
