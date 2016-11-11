# -*- coding: utf-8 -*-
"""
    boradevan.models.user
    ~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from boradevan.models import BaseModel


class User(BaseModel):

    id_field = 'email'
    table_name = 'users'

    def set_password(self, password):
        self['password'] = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self['password'], password)

    def set_access_type(self, access_type):
        self['access_type'] = access_type

    def generate_token(self, secret_key):
        return jwt.encode(dict(email=self['email'],
                               access_type=self['access_type']),
                          key=secret_key)

    @property
    def is_driver(self):
        from boradevan.models.driver import Driver
        return self['access_type'] == Driver.USER_TYPE

    @property
    def is_passenger(self):
        from boradevan.models.passenger import Passenger
        return self['access_type'] == Passenger.USER_TYPE

    @classmethod
    def decode_token(cls, token, secret_key):
        return jwt.decode(token, key=secret_key)

    @classmethod
    def get_by_email(cls, email):
        return cls.get_by_key(email)
