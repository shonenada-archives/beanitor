from flask import request
from flask.ext.babel import Babel

from beanitor.beanstalk import Beanstalkc


babel = Babel()
beanstalk = Beanstalkc()


def setup_babel(app):
    babel.init_app(app)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(['en', 'zh'])
