from flask.ext.script import Manager

from beanitor.app import create_app


application = create_app('beanitor')
manager = Manager(application)


if __name__ == '__main__':
    manager.run()
