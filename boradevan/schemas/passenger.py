# -*- coding: utf-8 -*-
"""
    boradevan.schemas.itinerary.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""


from marshmallow import Schema, fields
from boradevan.schemas.address import AddressSchema


class PassengerSchema(Schema):

    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)
    boarding_address = fields.Nested(AddressSchema, required=True)
