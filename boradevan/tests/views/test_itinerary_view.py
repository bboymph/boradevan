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
            'timestart': '06:00',
            'endtime': '07:00',
            'destination': {
                'street': 'Street 1',
                'neighborhood': 'Neigh 1',
                'city': 'City 1',
                'state': 'AB',
                'latitude': -27.4578,
                'longitude': -45.8796
            },
            'weekdays': 'Seg Ter Qua Qui Sex'
        }), headers={
            'Content-Type': 'application/json',
            'Authorization': self.test_driver_token
        })

        self.assertEqual(response.status_code, 201)

        itinerary = Itinerary.find_one({
            'name': 'IT123',
            'timestart': '06:00',
            'endtime': '07:00',
            'destination': {
                'street': 'Street 1',
                'neighborhood': 'Neigh 1',
                'city': 'City 1',
                'state': 'AB',
                'latitude': -27.4578,
                'longitude': -45.8796
            },
            'weekdays': 'Seg Ter Qua Qui Sex',
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
            'email': 'test@example.com',
            'name': 'Driver Test',
            'phone': '912345678'
        }), headers={
            'Content-Type': 'application/json',
            'Authorization': self.test_driver_token
        })

        self.assertEqual(response.status_code, 201)


class ItineraryGetDriverItineraries(AppTestCase):

    def setUp(self):
        super(ItineraryGetDriverItineraries, self).setUp()

        self.test_driver = Driver(email='test@example.com')
        Driver.insert(self.test_driver)

        secret_key = self.app.config['SECRET_KEY']
        self.test_driver_token = self.test_driver.generate_token(secret_key)

        self.test_itinerary = Itinerary(id='1', name='test_itinerary', owner='test@example.com',
                                        timestart='12:00', endtime='13:00', weekdays='Seg')
        Itinerary.insert(self.test_itinerary)

    def test_get_driver_itineraries(self):
        url = url_for('itinerary.list_driver_itineraries')

        response = self.client.post(url, data=json.dumps({
            'email': 'test@example.com'
        }), headers={
            'Content-Type': 'application/json',
            'Authorization': self.test_driver_token
        })

        self.assertEqual(response.status_code, 201)

class ItineraryUpdateDriverLocation(AppTestCase):

    def setUp(self):
        super(ItineraryUpdateDriverLocation, self).setUp()

        self.test_driver = Driver(email='test@example.com')
        Driver.insert(self.test_driver)

        secret_key = self.app.config['SECRET_KEY']
        self.test_driver_token = self.test_driver.generate_token(secret_key)

        self.test_itinerary = Itinerary(id='1', name='test_itinerary', owner='test@example.com',
                                        timestart='12:00', endtime='13:00', weekdays='Seg')
        Itinerary.insert(self.test_itinerary)

    def test_update_driver_location(self):
        url = url_for('itinerary.update_driver_location', itinerary_id='1')

        response = self.client.post(url, data=json.dumps({
            'latitude': -27.4578,
            'longitude': -45.8796
        }), headers={
            'Content-Type': 'application/json',
            'Authorization': self.test_driver_token
        })

        self.assertEqual(response.status_code, 201)
