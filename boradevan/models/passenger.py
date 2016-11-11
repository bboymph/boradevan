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

    def __init__(self, **kwargs):
        super(Passenger, self).__init__(**kwargs)
        self.set_access_type(self.USER_TYPE)
