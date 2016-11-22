# -*- coding: utf-8 -*-
"""
    boradevan.models.driver.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.models.user import User


class Driver(User):

    USER_TYPE = 'driver'

    table_name = 'users'

    def __init__(self, itineraries=[], **kwargs):
        super(Driver, self).__init__(itineraries=itineraries, **kwargs)
        self.set_access_type(Driver.USER_TYPE)

    def insert_itinerary(self, itinerary):
        self['itineraries'].append(itinerary['id'])

    @classmethod
    def get_all_drivers(cls, access_type):
        return cls.find({"access_type": access_type})
