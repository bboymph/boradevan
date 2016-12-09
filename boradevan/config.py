# -*- coding: utf-8 -*-
"""
    boradevan.config
    ~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from os import getenv


class BaseConfig(object):

    SECRET_KEY = 'change this in production'
    DATABASE_HOST = getenv('DATABASE_HOST', 'localhost')
    DATABASE_PORT = int(getenv('DATABASE_PORT', '28015'))
    DATABASE_NAME = getenv('DATABASE_NAME', 'boradevan')


class DevelopmentConfig(BaseConfig):

    DEBUG = True
    DATABASE_NAME = getenv('DATABASE_NAME', 'boradevan_dev')


class TestingConfig(BaseConfig):

    TESTING = True
    DATABASE_NAME = getenv('DATABASE_NAME', 'boradevan_test')

class ProductionConfig(BaseConfig):

    DEBUG = False
    TESTING = False


