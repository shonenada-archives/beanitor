from beanstalkc import Connection, SocketError


class _BeanstalkState(object):

    def __init__(self, client, app):
        self.client = client
        self.app = app


class Beanstalkc(object):
    '''A simple proxy object for beanstalk.'''

    def __init__(self, app=None):
        self._client = None
        self._connected = False

        if app is not None:
            self.init_app(app)

    def init_app(self, app, silent=True):
        app.config.setdefault('BEANSTALK_HOST', '127.0.0.1')
        app.config.setdefault('BEANSTALK_PORT', 11300)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['beanstalk'] = _BeanstalkState(self, app)

        try:
            self._client = Connection(
                host=app.config.get('BEANSTALK_HOST'),
                port=app.config.get('BEANSTALK_PORT'))
            self._connected = True
        except SocketError:
            if silent:
                self._client = None
                self._connected = False
            else:
                raise

    def __getattr__(self, name):
        return getattr(self._client, name)

    def is_connected(self):
        return self._connected is True
