# -*- coding: utf-8 -*-
"""
    boradevan.views.passenger.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Blueprint, request, jsonify, g

from boradevan.models.itinerary import Itinerary

from boradevan.permissions import login_required
from boradevan.schemas.notification_absence import NotificationAbsenceSchema
from boradevan.schemas.passenger import PassengerSchema
from boradevan.models.notification_absence import NotificationAbsence
from boradevan.models.passenger import Passenger
from boradevan.models.user import User


passenger = Blueprint('passenger', __name__)


@passenger.route('/', methods=['POST'])
@login_required
def create():
    data = request.get_json()

    itinerary = Itinerary.get_by_key(data['itinerary_id'])
    data.pop("itinerary_id")

    schema = PassengerSchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 400

    user = Passenger(**data)
    result = User.insert(user)

    itinerary.add_passenger(user)
    Itinerary.update(itinerary)

    if result['errors']:
        return jsonify({
            'errors': result['first_error']
        }), 409

    return jsonify({
        'email': user['email']
    }), 201


@passenger.route('/<itinerary_id>/messages', methods=['POST'])
@login_required
def notify(itinerary_id):
    data = request.get_json()

    itinerary = Itinerary.get_by_key(itinerary_id)

    if not itinerary:
        return jsonify({
            'errors': ['Itinerary not found']
        }), 404

    schema = NotificationAbsenceSchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 400

    notification = NotificationAbsence(**data)
    notification['itinerary_id'] = itinerary['id']
    notification['passenger_id'] = g.user['email']

    result = NotificationAbsence.insert(notification)

    if result['errors']:
        return jsonify({
            'errors': result['first_error']
        }), 409

    return jsonify({
        'message': notification['message']
    }), 201
