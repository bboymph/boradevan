# -*- coding: utf-8 -*-
"""
    boradevan.schemas.address
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from marshmallow import Schema, fields


class AddressSchema(Schema):

    street = fields.Str(required=True)
    neighborhood = fields.Str(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
