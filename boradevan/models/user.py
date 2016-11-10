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

    table_name = 'users'

    def set_password(self, password):
        self['password'] = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self['password'], password)

    def set_access_type(self, access_type):
        self['access_type'] = access_type

    def generate_token(self, secret_key):
        return jwt.encode(dict(email=self['email'],
                               access_type=self['access_type']), key=secret_key)

    @classmethod
    def decode_token(cls, token, secret_key):
        return jwt.decode(token, key=secret_key)

    @classmethod
    def get_by_email(cls, email):
        return cls.get_by_key(email)

    @classmethod
    def get_by_type(cls, access_type):
        return cls.get_by_type(access_type)
