# -*- coding: utf-8 -*-
"""
    boradevan.views.itinerary
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Blueprint, request, jsonify
from boradevan.schemas.itinerary import ItinerarySchema
from boradevan.models.itinerary import Itinerary


itinerary = Blueprint('itinerary', __name__)


@itinerary.route('/', methods=['POST'])
def create():
    data = request.get_json()

    schema = ItinerarySchema(strict=True)
    data, errors = schema.load(data)

    if errors:
        return jsonify({
            'errors': errors
        }), 400

    result = Itinerary.insert(Itinerary(**data))

    return jsonify({
        'id': result['generated_keys']
    }), 201
