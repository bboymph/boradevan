# -*- coding: utf-8 -*-
"""
    boradevan.models.itinerary.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.models.user import User


class Passenger(User):

    table_name = 'passengers'