# -*- coding: utf-8 -*-
"""
    boradevan.models.itinerary
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Zapen (see AUTHORS).
    :license: see LICENSE for more details.
"""

from boradevan.models import BaseModel


class AbsenceNotification(BaseModel):

    table_name = 'notification_absence'

    table_name = 'absence_notification'

    def __init__(self, **kwargs):
        super(AbsenceNotification, self).__init__(**kwargs)
