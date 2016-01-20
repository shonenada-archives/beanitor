from flask.ext.babel import lazy_gettext as _


def humanable_time(timestamp):
    days = float(timestamp) / 60.0 / 60.0 / 24.0
    return '%.2f %s' % (days, _('days'))


def setup_filters(app):
    filters = {
        'humanable_time': humanable_time,
    }
    for _name, _func in filters.iteritems():
        app.add_template_filter(_func, _name)
