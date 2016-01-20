# -*- coding: utf-8 -*-
import os
import json
import logging


ENV_CONFIG_PREFIX = 'BEANITOR_'


def _load_from_env(name, default=None, use_json=True):
    raw_value = os.environ.get(name, default)
    if raw_value is not None:
        if use_json:
            try:
                return json.loads(raw_value)
            except (TypeError, ValueError):
                return raw_value
            return raw_value
    return None


class Config(object):

    def __init__(self, update=None):
        self._configs = {}
        self._init_keys()
        if update:
            if not isinstance(update, dict):
                logging.warning('The update params is not dict instance.')
            else:
                self._update(update)

    def keys(self):
        return self._configs.keys()

    def iteriterms(self):
        return iter(
            [(k, self.__getattr__(k))
             for k, _ in self._configs.iteriterms()])

    def __getattr__(self, name):
        default = self._configs.get(name, None)
        return _load_from_env(name, default=default)

    def __getitem__(self, name):
        return self.__getattr__(name)

    def _update(self, update):
        self._configs.update(update)

    def _init_keys(self):
        for key in os.environ:
            if key.startswith(ENV_CONFIG_PREFIX):
                self._configs.setdefault(key[len(ENV_CONFIG_PREFIX):],
                                         os.environ.get(key))


CONFIG = Config()
