from flask import Blueprint
from beanstalkc import SocketError

from beanitor.exts import beanstalk


bp = Blueprint('master', __name__)


@bp.route('')
def index():
    return render_template('index.html')


@bp.route('/stat')
def stat():
    stats = client.stats()
    return render_template('stats.html', stats)
