# -*- coding: utf-8 -*-
"""
    boradevan.views.itinerary.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Blueprint, request, jsonify
from boradevan.permissions import login_required
from boradevan.schemas.passenger import PassengerSchema
from boradevan.models.passenger import Passenger
from boradevan.models.user import User


passenger = Blueprint('passenger', __name__)


@passenger.route('/', methods=['POST'])
@login_required
def create():
    data = request.get_json()

    schema = PassengerSchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 400

    user = Passenger(**data)
    result = User.insert(user)

    if result['errors']:
        return jsonify({
            'errors': result['first_error']
        }), 409

    return jsonify({
        'email': user['email']
    }), 201
