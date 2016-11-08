#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    run boradevan in development mode
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from flask_script import Manager
from boradevan import create_app
from boradevan.config import DevelopmentConfig

app = create_app(DevelopmentConfig())

manager = Manager(app)


if __name__ == "__main__":
    manager.run()
