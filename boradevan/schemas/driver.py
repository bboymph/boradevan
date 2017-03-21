# -*- coding: utf-8 -*-
"""
    boradevan.schemas.__init__.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""


from marshmallow import Schema, fields


class DriverSchema(Schema):

    name = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    phone = fields.Str(required=True)
