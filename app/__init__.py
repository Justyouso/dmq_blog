# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 20-1-8 下午2:10

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

# from app.exts import mgo_client
# from app.middlewares import AuthMiddleware

mail = Mail()
db = SQLAlchemy()

business_modules = [
    # "app.login:login",
    "app.article:article"
]


def register_extensions(app):
    # redis_client.init_app(app)
    pass


def register_blueprints(app, blueprints: list):
    for bp in blueprints:
        module = import_string(bp)
        app.register_blueprint(module, url_prefix="")


def register_middleware(app, middlewares):
    app.wsgi_app = middlewares(app.wsgi_app)


def create_app(config):
    app = Flask(config.APP_NAME)
    app.config.from_object(config)
    # register_middleware(app, AuthMiddleware)
    # register_extensions(app)
    register_blueprints(app, business_modules)
    db.init_app(app)
    mail.init_app(app)
    return app
