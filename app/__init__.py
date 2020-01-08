# @Time    : 2019-06-01 08:09
# @Author  : __apple
from base import log
from base.log import start_log
from .app import Flask


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


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
    register_plugin(app)
    startup_log()
    return app
