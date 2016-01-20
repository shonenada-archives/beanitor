# -*- coding: utf-8 -*-
'''
Beanstalkd Procotol.

https://raw.githubusercontent.com/kr/beanstalkd/master/doc/protocol.txt
'''
from flask import Blueprint, render_template, redirect, url_for, request, abort
from beanstalkc import CommandFailed

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


@bp.route('/tubes')
def tubes():
    tubes = beanstalk.tubes()
    return render_template('tubes.html', tubes=tubes)


@bp.route('/tubes/<name>')
def tube(name):
    try:
        tube = beanstalk.stats_tube(name).items()
    except CommandFailed:
        return abort(404)

    return render_template('tube.html', tube=tube)


@bp.route('/unavailable')
def unavailable():
    return 'Cannot connect to %s:%s' % (CONFIG.BEANSTALK_HOST,
                                        CONFIG.BEANSTALK_PORT)
