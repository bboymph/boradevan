# -*- coding: utf-8 -*-
"""
    boradevan.tests
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask_testing import TestCase
from boradevan import create_app
from boradevan.db import db, drop_database, setup_database
from boradevan.config import TestingConfig


class AppTestCase(TestCase):

    def create_app(self):
        app = create_app(TestingConfig())
        return app

    def setUp(self):
        drop_database(db)
        setup_database(db)
