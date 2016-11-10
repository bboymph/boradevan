# -*- coding: utf-8 -*-
"""
    boradevan.tests.views.test_passenger_view
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import url_for, json
from boradevan.tests import AppTestCase
from boradevan.models.user import User
from boradevan.models.passenger import Passenger


class PassengerViewTestCase(AppTestCase):

    def setUp(self):
        self.test_user = User(email='test@example.com')
        self.test_user.set_access_type('passenger')
        User.insert(self.test_user)

        secret_key = self.app.config['SECRET_KEY']
        self.test_user_token = self.test_user.generate_token(secret_key)

    def test_create_passenger(self):
        url = url_for('passenger.create')

        response = self.client.post(url, data=json.dumps({
            'name': 'passenger1',
            'email': 'passenger1@example.com',
            'phone': '12345678',
            'boarding_address': {
                'street': 'Street 1',
                'neighborhood': 'Neigh 1',
                'city': 'City 1',
                'state': 'AB',
                'lat': -27.4578,
                'lng': -45.8796
            }
        }), headers={
            'Content-Type': 'application/json',
            'Authorization': self.test_user_token
        })

        self.assertEqual(response.status_code, 201)

        passenger = Passenger.find_one({
            'name': 'passenger1',
            'email': 'passenger1@example.com',
            'phone': '12345678',
            'boarding_address': {
                'street': 'Street 1',
                'neighborhood': 'Neigh 1',
                'city': 'City 1',
                'state': 'AB',
                'lat': -27.4578,
                'lng': -45.8796
            }
        })

        self.assertIsNotNone(passenger)