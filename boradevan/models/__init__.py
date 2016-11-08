# -*- coding: utf-8 -*-
"""
    boradevan.models
    ~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

import rethinkdb as r
from boradevan.db import db


class BaseModel(dict):

    table_name = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = value

    @classmethod
    def insert(cls, obj):
        return r.table(cls.table_name) \
                .insert(obj) \
                .run(db)

    @classmethod
    def get_by_key(cls, key):
        doc = r.table(cls.table_name) \
               .get(key) \
               .run(db)

        return cls(**doc)
