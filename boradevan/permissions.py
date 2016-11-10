# -*- coding: utf-8 -*-
"""
    boradevan.auth
    ~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from functools import wraps
from flask import g, jsonify


def login_required(fn):
    @wraps(fn)
    def wrapped_fn(*args, **kwargs):
        if 'user' not in g or g.user is None:
            return jsonify({
                'message': 'Not Authorized'
            }), 401
        return fn(*args, **kwargs)
    return wrapped_fn
