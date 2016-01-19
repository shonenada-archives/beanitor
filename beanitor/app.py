# -*- coding: utf-8 -*-
import os

from flask import Flask
from beanitor.exts import beanstalk

from beanitor.views import bp


def create_app(name=None):
    app = Flask(name or __name__)

    app.debug = bool(int(os.environ.get('DEBUG', False)))

    beanstalk.init_app(app)

    app.register_blueprint(bp)

    return app
