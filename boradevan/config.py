# -*- coding: utf-8 -*-
"""
    boradevan.config
    ~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""


class BaseConfig(object):
    pass


class DevelopmentConfig(BaseConfig):

    DEBUG = True


class TestingConfig(BaseConfig):

    TESTING = True
