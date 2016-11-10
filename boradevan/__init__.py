# -*- coding: utf-8 -*-
"""
    boradeva
    ~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask import Flask, request, g
from boradevan.blueprints.auth import auth
from boradevan.blueprints.itinerary import itinerary
from boradevan.blueprints.passenger import passenger
from boradevan.models.user import User
from boradevan.db import db, setup_database


def create_app(config):

    app = Flask(__name__)

    app.config.from_object(config)
    app.config.from_envvar('BORADEVAN_CONFIG', silent=True)

    with app.app_context():
        setup_database(db)

    @app.before_request
    def auth_token():
        token = request.headers.get('Authorization')
        if not token:
            return

        payload = User.decode_token(token, app.config['SECRET_KEY'])
        g.user = User.get_by_email(payload['email'])

    @app.route('/')
    def home():
        return 'ok'

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(itinerary, url_prefix='/itinerary')
    app.register_blueprint(passenger, url_prefix='/passenger')

    return app
