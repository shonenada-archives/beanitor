# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

from beanitor.exts import beanstalk


bp = Blueprint('master', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/stats')
def stat():
    stats = beanstalk.stats()
    return render_template('stats.html', stats=stats)
