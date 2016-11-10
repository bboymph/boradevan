# -*- coding: utf-8 -*-
"""
    boradevan.tests.views.test_driver_view
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import url_for, json
from boradevan.tests import AppTestCase
from boradevan.models.driver import Driver


class DriverViewTestCase(AppTestCase):

    def test_create_driver(self):
        url = url_for('driver.create')

        response = self.client.post(url, data=json.dumps({
            'name': 'driver1',
            'email': 'driver1@example.com',
            'password': 'secret123',
            'phone': '12345678'
        }), headers={
            'Content-Type': 'application/json',
        })

        self.assertEqual(response.status_code, 201)

        driver = Driver.find_one({
            'name': 'driver1',
            'email': 'driver1@example.com',
            'phone': '12345678'
        })

        self.assertIsNotNone(driver)
