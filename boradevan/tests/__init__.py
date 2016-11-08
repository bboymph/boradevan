# -*- coding: utf-8 -*-
"""
    boradevan.tests
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask_testing import TestCase
from boradevan import create_app
from boradevan.config import TestingConfig


class AppTestCase(TestCase):

    def create_app(self):
        app = create_app(TestingConfig())
        return app
