# -*- coding: utf-8 -*-
"""
    boradevan.schemas.notificationAbsence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

import re
from marshmallow import Schema, ValidationError, fields, validates
from boradevan.schemas.address import AddressSchema


class NotificationAbsenceSchema(Schema):

    date = fields.Str(required=True)
    message = fields.Str(required=True)
    email = fields.Str(required=True)
