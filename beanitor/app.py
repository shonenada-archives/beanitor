# -*- coding: utf-8 -*-
from flask import Flask
from beanitor.exts import beanstalk

from beanitor.config import CONFIG
from beanitor.views import bp


def create_app(name=None):
    app = Flask(name or __name__)

    app.config.update(CONFIG)

    beanstalk.init_app(app)

    app.register_blueprint(bp)

    return app
