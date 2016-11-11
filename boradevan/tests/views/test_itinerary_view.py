# -*- coding: utf-8 -*-
"""
    boradevan.tests.views.test_itinerary_view
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import url_for, json
from boradevan.tests import AppTestCase
from boradevan.models.driver import Driver
from boradevan.models.itinerary import Itinerary


class ItineraryCreateViewTestCase(AppTestCase):

    def setUp(self):
        self.test_driver = Driver(email='test@example.com')
        Driver.insert(self.test_driver)

        secret_key = self.app.config['SECRET_KEY']
        self.test_driver_token = self.test_driver.generate_token(secret_key)

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
            'Authorization': self.test_driver_token
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
            },
            'owner': 'test@example.com',
            'drivers': []
        })

        self.assertIsNotNone(itinerary)


class ItineraryAddPartnerTestCase(AppTestCase):

    def setUp(self):
        super(ItineraryAddPartnerTestCase, self).setUp()

        self.test_driver = Driver(email='test@example.com')
        Driver.insert(self.test_driver)

        secret_key = self.app.config['SECRET_KEY']
        self.test_driver_token = self.test_driver.generate_token(secret_key)

        self.test_itinerary = Itinerary(id='1', name='test_itinerary')
        Itinerary.insert(self.test_itinerary)

    def test_add_partner_itinerary(self):
        url = url_for('itinerary.add_partner', itinerary_id='1')

        response = self.client.post(url, data=json.dumps({
            'email': 'test@example.com'
        }), headers={
            'Content-Type': 'application/json',
            'Authorization': self.test_driver_token
        })

        self.assertEqual(response.status_code, 201)
