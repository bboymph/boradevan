# -*- coding: utf-8 -*-
"""
    boradevan.tests.test_home_view
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.tests import AppTestCase


class HomeViewTestCase(AppTestCase):

    def test_home_should_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
