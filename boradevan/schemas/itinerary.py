# -*- coding: utf-8 -*-
"""
    boradevan.schemas.itinerary
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

import re
from marshmallow import Schema, ValidationError, fields, validates
from boradevan.schemas.address import AddressSchema


class ItinerarySchema(Schema):

    _time_regex = re.compile(r'^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$')

    name = fields.Str(required=True)
    start_time = fields.Str(required=True)
    end_time = fields.Str(required=True)
    destination = fields.Nested(AddressSchema, required=True)

    def _validate_time(self, data):
        if self._time_regex.match(data) is None:
            raise ValidationError('Invalid time')

    @validates('start_time')
    def validate_start_time(self, data):
        self._validate_time(data)

    @validates('end_time')
    def validate_end_time(self, data):
        self._validate_time(data)
