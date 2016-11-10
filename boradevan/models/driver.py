# -*- coding: utf-8 -*-
"""
    boradevan.models.driver.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.models.user import User


class Driver(User):

    table_name = 'drivers'
