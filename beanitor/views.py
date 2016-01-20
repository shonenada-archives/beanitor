# -*- coding: utf-8 -*-
'''
Beanstalkd Procotol.

https://raw.githubusercontent.com/kr/beanstalkd/master/doc/protocol.txt
'''
from flask import Blueprint, render_template, redirect, url_for, request

from beanitor.config import CONFIG
from beanitor.exts import beanstalk


bp = Blueprint('master', __name__)


def check():
    if (not request.endpoint == 'master.unavailable' and
            not beanstalk.is_connected()):
        return redirect(url_for('master.unavailable'))


bp.before_request(check)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/stats')
def stats():
    stats = beanstalk.stats()
    return render_template('stats.html', stats=stats)


@bp.route('/unavailable')
def unavailable():
    return 'Cannot connect to %s:%s' % (CONFIG.BEANSTALK_HOST,
                                        CONFIG.BEANSTALK_PORT)
