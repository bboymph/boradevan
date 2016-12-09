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

    def __init__(self, driver_location={}, drivers=[], partners=[], **kwargs):
        super(Itinerary, self).__init__(driver_location=driver_location,
                                        drivers=drivers,
                                        partners=partners,
                                        **kwargs)

    def add_partner(self, driver):
        self['drivers'].append(driver['email'])

    def add_passenger(self, passenger):
        self['passengers'].append({'email': passenger['email'],
                                   'name': passenger['name'],
                                   'boarding_address': passenger['boarding_address']})

    def update_driver_location(self, location):
        self['driver_location'] = {'street': location['street'],
                                   'neighborhood': location['neighborhood'],
                                   'city': location['city'],
                                   'state': location['state'],
                                   'latitude': location['latitude'],
                                   'longitude': location['longitude']}

    @classmethod
    def find_by_owner(cls, email):
        return cls.find({"owner": email})

    @classmethod
    def find_by_passenger(cls, email):
        return cls.find_passenger_itineraries(email)
