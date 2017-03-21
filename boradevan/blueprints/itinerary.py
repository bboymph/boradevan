# -*- coding: utf-8 -*-
"""
    boradevan.views.itinerary.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


@itinerary.route('/driver', methods=['GET'])
@login_required
def list_driver_itineraries():

    itineraries = Itinerary.find_by_owner(g.user['email'])

    return jsonify({"objects": list(itineraries)}), 201


@itinerary.route('/passenger', methods=['GET'])
@login_required
def list_passenger_itineraries():

    itineraries = Itinerary.find_by_passenger(g.user['email'])

    return jsonify({"objects": list(itineraries)}), 201


@itinerary.route('/<itinerary_id>/drivers', methods=['POST'])
@login_required
def add_partner(itinerary_id):
    data = request.get_json()
    print(data)
    itinerary = Itinerary.get_by_key(itinerary_id)

    if not itinerary:
        return jsonify({
            'errors': ['Itinerary not found']
        }), 404

    '''schema = ItineraryAddPartnerSchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 409'''

    driver = Driver.get_by_email(data['name'])
    if not driver:
        return jsonify({
            'errors': ['Driver not found.']
        }), 404

    itinerary.add_partner(driver)
    Itinerary.update(itinerary)

    return jsonify({
        'id': itinerary_id
    }), 201

@itinerary.route('/<itinerary_id>/location/drivers', methods=['POST'])
@login_required
def update_driver_location(itinerary_id):
    data = request.get_json()

    itinerary = Itinerary.get_by_key(itinerary_id)

    if not itinerary:
        return jsonify({
            'errors': ['Itinerary not found']
        }), 404

    driver = Driver.get_by_email(g.user['email'])

    if not driver:
        return jsonify({
            'errors': ['Driver not found.']
        }), 404

    itinerary.update_driver_location(data)
    Itinerary.update(itinerary)

    return jsonify({
        'id': itinerary_id
    }), 201


@itinerary.route('/<itinerary_id>/location', methods=['GET'])
@login_required
def get_driver_location(itinerary_id):

    itinerary = Itinerary.get_by_key(itinerary_id)
    print(itinerary['driver_location'])

    return jsonify(itinerary['driver_location']), 201
