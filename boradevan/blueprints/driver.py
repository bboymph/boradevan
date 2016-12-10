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
from boradevan.permissions import login_required

driver = Blueprint('drivers', __name__)


@driver.route('/', methods=['POST'])
def create():
    data = request.get_json()

    print(request.headers)

    schema = DriverSchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 400

    user = Driver(itineraries=[], **data)
    user.set_password(data['password'])

    result = User.insert(user)

    if result['errors']:
        return jsonify({
            'errors': result['first_error']
        }), 409

    return jsonify({
        'email': user['email']
    }), 201


@driver.route('/list')
@login_required
def list_drivers():
    drivers = Driver.get_all_drivers(Driver.USER_TYPE)

    return jsonify({"objects": list(drivers)}), 201
