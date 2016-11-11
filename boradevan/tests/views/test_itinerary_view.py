# -*- coding: utf-8 -*-
"""
    boradevan.tests.views.test_itinerary_view
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import url_for, json
from boradevan.tests import AppTestCase
from boradevan.models.user import User
from boradevan.models.itinerary import Itinerary


class ItineraryViewTestCase(AppTestCase):

    def setUp(self):
        self.test_user = User(email='test@example.com')
        self.test_user.set_access_type('driver')
        User.insert(self.test_user)

        secret_key = self.app.config['SECRET_KEY']
        self.test_user_token = self.test_user.generate_token(secret_key)

        self.test_itinerary = Itinerary(id='1', name='test_itinerary', drivers=[])
        Itinerary.insert(self.test_itinerary)

    def test_create_itinerary(self):
        url = url_for('itinerary.create')

        response = self.client.post(url, data=json.dumps({
            'name': 'IT123',
            'start_time': '06:00',
            'end_time': '07:00',
            'destination': {
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

        itinerary = Itinerary.find_one({
            'name': 'IT123',
            'start_time': '06:00',
            'end_time': '07:00',
            'destination': {
                'street': 'Street 1',
                'neighborhood': 'Neigh 1',
                'city': 'City 1',
                'state': 'AB',
                'lat': -27.4578,
                'lng': -45.8796
            }
        })

        self.assertIsNotNone(itinerary)

    def test_add_partner_itinerary(self):
        url = url_for('itinerary.add_partner', itinerary_id='1')

        response = self.client.post(url, data=json.dumps({
            'name': 'motorista parceiro',
            'email': 'partner@example.com'
        }), headers={
            'Content-Type': 'application/json',
            'Authorization': self.test_user_token
        })

        self.assertEqual(response.status_code, 201)
