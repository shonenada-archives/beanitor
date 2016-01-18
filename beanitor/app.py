from flask import Flask

from beanitor.exts import beanstalk


def create_app(name=None):
    app = Flask(name or __name__)

    beanstalk.init_app(app)

    return app
