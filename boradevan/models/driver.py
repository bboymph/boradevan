# -*- coding: utf-8 -*-
"""
    boradevan.models.driver.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.models.user import User


class Driver(User):

    USER_TYPE = 'driver'

    table_name = 'users'

    def __init__(self, **kwargs):
        super(Driver, self).__init__(**kwargs)
        self.set_access_type(Driver.USER_TYPE)
