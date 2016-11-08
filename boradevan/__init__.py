# -*- coding: utf-8 -*-
"""
    boradeva
    ~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Flask


def create_app(config):

    app = Flask(__name__)

    app.config.from_object(config)
    app.config.from_envvar('BORADEVAN_CONFIG', silent=True)

    @app.route('/')
    def home():
        return 'ok'

    return app
