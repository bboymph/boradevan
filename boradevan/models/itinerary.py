# -*- coding: utf-8 -*-
"""
    boradevan.models.itinerary
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.models import BaseModel
import rethinkdb as r
from boradevan.db import db


class Itinerary(BaseModel):

    table_name = 'itineraries'

    def add_partner(self, itinerary, email):
        return r.table(self.table_name).get(itinerary)\
                .update({'drivers': r.row['drivers'].append(email)}).run(db)
