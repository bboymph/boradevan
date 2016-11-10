# -*- coding: utf-8 -*-
"""
    boradevan.views.driver.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Blueprint, request, jsonify
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
    result = Driver.insert(driver)

    if result['errors']:
        return jsonify({
            'errors': result['first_error']
        }), 409

    return jsonify({
        'email': driver['email']
    }), 201
