# @Time    : 2019-06-01 08:09
# @Author  : __apple
import sys
from .app import Flask
from base import log
from base.log import start_log
from cmds import lint


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_cmd(app):
    app.cli.add_command(lint.lint)


def register_plugin(app):
    from model.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def startup_log():
    # 启动日志
    start_log(file_path="apple")
    log.logging.info('[INFO] start http server listening')


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')
    register_blueprints(app)
    register_cmd(app)
    register_plugin(app)
    startup_log()
    return app
