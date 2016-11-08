# -*- coding: utf-8 -*-
"""
    boradevan.tests.models.test_user_model
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from unittest import TestCase
from boradevan.models.user import User


class UserModelTestCase(TestCase):

    def test_token(self):
        user = User(email='test@example.com')
        token = user.generate_token('secret123')

        self.assertIsNotNone(token)

        data = User.decode_token(token, 'secret123')

        self.assertEqual(data['email'], 'test@example.com')

    def test_password(self):
        user = User(email='test@example.com')

        user.set_password('secret123')

        self.assertNotEqual(user['password'], 'secret123')
        self.assertTrue(user.check_password('secret123'))
