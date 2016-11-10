# -*- coding: utf-8 -*-
"""
    boradevan.db
    ~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

import rethinkdb as r
from flask import current_app
from werkzeug.local import LocalProxy


_tables = {
    'users': {
        'primary_key': 'email'
    },
    'itineraries': {},
    'passengers': {
        'primary_key': 'email'
    }
}


def setup_database(db):
    db_name = current_app.config['DATABASE_NAME']

    if db_name not in r.db_list().run(db):
        r.db_create(db_name).run(db)

    tables = r.table_list().run(db)

    for table_name, options in _tables.items():
        if table_name in tables:
            continue

        r.table_create(table_name, **options).run(db)


def _db():
    db_conn = r.connect(
        current_app.config['DATABASE_HOST'],
        current_app.config['DATABASE_PORT'])
    db_conn.use(current_app.config['DATABASE_NAME'])

    return db_conn

db = LocalProxy(_db)
