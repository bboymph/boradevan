# -*- coding: utf-8 -*-
"""
    boradevan.views.itinerary
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Blueprint, g, request, jsonify
from boradevan.permissions import login_required
from boradevan.schemas.itinerary import ItinerarySchema
from boradevan.models.itinerary import Itinerary
from boradevan.models.driver import Driver


itinerary = Blueprint('itinerary', __name__)


@itinerary.route('/', methods=['POST'])
@login_required
def create():
    data = request.get_json()

    schema = ItinerarySchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 400

    itinerary = Itinerary(owner=g.user['email'],
                          drivers=[],
                          passengers=[], **data)
    result = Itinerary.insert(itinerary)

    return jsonify({
        'id': result['generated_keys']
    }), 201


@itinerary.route('/<itinerary_id>/drivers', methods=['POST'])
@login_required
def add_partner(itinerary_id):
    data = request.get_json()

    driver = Driver(**data)
    itinerary = Itinerary()
    result = itinerary.add_partner(itinerary_id, email=driver)

    if result['errors']:
        return jsonify({
            'error': result['first_error']
        }), 409

    return jsonify({
        'id': itinerary_id
    }), 201
