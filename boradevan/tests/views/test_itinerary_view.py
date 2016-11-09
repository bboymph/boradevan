# -*- coding: utf-8 -*-
"""
    boradevan.tests.views.test_itinerary_view
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import url_for, json
from boradevan.tests import AppTestCase
from boradevan.models.itinerary import Itinerary


class ItineraryViewTestCase(AppTestCase):

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
            'Content-Type': 'application/json'
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
