# -*- coding: utf-8 -*-
"""
    boradevan.tests.test_auth_view
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import url_for, json
from boradevan.tests import AppTestCase
from boradevan.models.driver import Driver
from boradevan.models.passenger import Passenger


class DriverAuthViewTestCase(AppTestCase):

    def setUp(self):
        super(DriverAuthViewTestCase, self).setUp()

        self.user_driver = Driver(name='Test',
                                  email='driver@example.com')
        self.user_driver.set_password('secret123')
        Driver.insert(self.user_driver)

    def test_user_driver_auth_ok(self):
        response = self.client.post(url_for('auth.login'), data=json.dumps({
            'email': 'driver@example.com',
            'access_type': 'driver',
            'password': 'secret123'
        }), headers={
            'Content-Type': 'application/json'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.json)

    def test_user_driver_auth_fail(self):
        response = self.client.post(url_for('auth.login'), data=json.dumps({
            'email': 'driver@example.com',
            'access_type': 'driver',
            'password': 'wrong789'
        }), headers={
            'Content-Type': 'application/json'
        })

        self.assertEqual(response.status_code, 401)
        self.assertTrue('token' not in response.json)


class PassengerAuthViewTestCase(AppTestCase):

    def setUp(self):
        super(PassengerAuthViewTestCase, self).setUp()

        self.user_passenger = Passenger(name='Test',
                                        email='passenger@example.com')
        self.user_passenger.set_password('secret123')
        Passenger.insert(self.user_passenger)

    def test_user_passenger_auth_ok(self):
        response = self.client.post(url_for('auth.login'), data=json.dumps({
            'email': 'passenger@example.com',
            'access_type': 'passenger',
            'password': 'secret123'
        }), headers={
            'Content-Type': 'application/json'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.json)

    def test_user_passenger_auth_fail(self):
        response = self.client.post(url_for('auth.login'), data=json.dumps({
            'email': 'passenger@example.com',
            'access_type': 'passenger',
            'password': 'wrong789'
        }), headers={
            'Content-Type': 'application/json'
        })

        self.assertEqual(response.status_code, 401)
        self.assertTrue('token' not in response.json)
