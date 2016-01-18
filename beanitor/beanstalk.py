from beanstalkc import Connection


class _BeanstalkState(object):

    def __init__(self, client, app):
        self.client = client
        self.app = app


class Beanstalkc(object):
    '''A simple proxy object for beanstalk.'''

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('BEANSTALK_HOST', '127.0.0.1')
        app.config.setdefault('BEANSTALK_PORT', 11300)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['beanstalk'] = _BeanstalkState(self, app)

        self._client = Connection(
            host=app.config.get('BEANSTALK_HOST'),
            port=app.config.get('BEANSTALK_PORT'))

    def __getattr__(self, name):
        return getattr(self._client, name)
