# -*- coding: utf-8 -*-
"""
    boradevan.models.itinerary
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.models import BaseModel


class Itinerary(BaseModel):

    table_name = 'itineraries'

    def __init__(self, drivers=[], partners=[], **kwargs):
        super(Itinerary, self).__init__(drivers=drivers,
                                        partners=partners,
                                        **kwargs)

    def add_partner(self, driver):
        self['partners'].append(driver['email'])

    def add_passenger(self, passenger):
        self['passengers'].append({'email': passenger['email'],
                                   'name': passenger['name'],
                                   'boarding_address': passenger['boarding_address']})

    @classmethod
    def find_by_owner(cls, email):
        return cls.find({"owner": email})
