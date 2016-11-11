# -*- coding: utf-8 -*-
"""
    boradevan.views.itinerary
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Blueprint, g, request, jsonify
from boradevan.permissions import login_required
from boradevan.schemas.itinerary import (
        ItinerarySchema,
        ItineraryAddPartnerSchema
)
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
    result = Itinerary.insert(itinerary, return_changes=True)

    itinerary = Itinerary(**result['changes'][0]['new_val'])

    g.user.insert_itinerary(itinerary)
    Driver.update(g.user)

    return jsonify({
        'id': itinerary.get_id()
    }), 201


@itinerary.route('/<itinerary_id>/drivers', methods=['POST'])
@login_required
def add_partner(itinerary_id):
    data = request.get_json()

    itinerary = Itinerary.get_by_key(itinerary_id)

    if not itinerary:
        return jsonify({
            'errors': ['Itinerary not found']
        }), 404

    schema = ItineraryAddPartnerSchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 409

    driver = Driver.get_by_email(data['email'])
    if not driver:
        return jsonify({
            'errors': ['Driver not found.']
        }), 404

    itinerary.add_partner(driver)
    Itinerary.update(itinerary)

    return jsonify({
        'id': itinerary_id
    }), 201
