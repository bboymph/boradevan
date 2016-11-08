# -*- coding: utf-8 -*-
"""
    boradevan.schemas.auth
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from marshmallow import Schema, fields


class LoginSchema(Schema):

    email = fields.Email(required=True)
    password = fields.Str(required=True)
