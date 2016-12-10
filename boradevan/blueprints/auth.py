# -*- coding: utf-8 -*-
"""
    boradevan.views.auth.py
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Blueprint, current_app, request, jsonify
from boradevan.models.user import User
from boradevan.schemas.auth import LoginSchema

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    print(request.headers)
    data = request.get_json()

    schema = LoginSchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify(dict(errors=errors)), 400

    user = User.get_by_email(data['email'])

    if user is None or not user.check_password(data['password']):
        return jsonify({
            'errors': ['Wrong email/password']
        }), 401

    secret_key = current_app.config['SECRET_KEY']

    return jsonify({
        'token': user.generate_token(secret_key),
        'access_type': user['access_type']
    })
