# -*- coding: utf-8 -*-
"""
    boradevan.models.itinerary.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.models.user import User


class Passenger(User):

    USER_TYPE = 'passenger'

    table_name = 'users'

    def __init__(self, itineraries=[], **kwargs):
        super(Passenger, self).__init__(itineraries=itineraries, **kwargs)
        self.set_access_type(self.USER_TYPE)

    def insert_itinerary(self, itinerary):
        self['itineraries'].append(itinerary['id'])
