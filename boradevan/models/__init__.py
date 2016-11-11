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

    id_field = 'id'
    table_name = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self[key] = value

    def get_id(self):
        return self[self.id_field]

    @classmethod
    def insert(cls, obj, **kwargs):
        return r.table(cls.table_name) \
                .insert(obj, **kwargs) \
                .run(db)

    @classmethod
    def update(cls, obj):
        return r.table(cls.table_name) \
                .get(obj[cls.id_field]) \
                .update(obj) \
                .run(db)

    @classmethod
    def get_by_key(cls, key):
        doc = r.table(cls.table_name) \
               .get(key) \
               .run(db)

        return cls(**doc)

    @classmethod
    def find_one(cls, filters):
        for doc in r.table(cls.table_name) \
                    .filter(filters) \
                    .limit(1) \
                    .run(db):
            return doc
