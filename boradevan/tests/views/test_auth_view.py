# -*- coding: utf-8 -*-
"""
    boradevan.tests.test_auth_view
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import url_for, json
from boradevan.tests import AppTestCase
from boradevan.models.user import User


class AuthViewTestCase(AppTestCase):

    def setUp(self):
        super(AuthViewTestCase, self).setUp()

        self.user1 = User(email='test@example.com')
        self.user1.set_password('secret123')

        User.insert(self.user1)

    def test_user_auth_ok(self):
        response = self.client.post(url_for('auth.login'), data=json.dumps({
            'email': 'test@example.com',
            'password': 'secret123'
        }), headers={
            'Content-Type': 'application/json'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.json)

    def test_user_auth_fail(self):
        response = self.client.post(url_for('auth.login'), data=json.dumps({
            'email': 'test@example.com',
            'password': 'wrong789'
        }), headers={
            'Content-Type': 'application/json'
        })

        self.assertEqual(response.status_code, 401)
        self.assertTrue('token' not in response.json)
