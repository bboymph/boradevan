# -*- coding: utf-8 -*-
"""
    boradevan.views.driver.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Blueprint, request, jsonify

from boradevan.models.user import User
from boradevan.schemas.driver import DriverSchema
from boradevan.models.driver import Driver


driver = Blueprint('driver', __name__)


@driver.route('/', methods=['POST'])
def create():
    data = request.get_json()

    schema = DriverSchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 400


    driver = Driver(**data)

    user = User(name=driver['name'], email=driver['email'])
    user.set_access_type('driver')
    user.set_password(driver['password'])

    del driver['password']
    result = Driver.insert(driver)

    if result['errors']:
        return jsonify({
            'errors': result['first_error']
        }), 409

    User.insert(user)

    return jsonify({
        'email': driver['email']
    }), 201
