# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils import timezone

from health.models import MedicationAdministration as MA
from health.models import MedicationRecurrence as MR


class MedicationNotificationsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.dtend = timezone.localtime()

    def __call__(self, request):
        schedules = MR.objects.filter(complete=False).filter(
            start__lte=timezone.localdate())

        for schedule in schedules:
            self.set_notifications(schedule)

        response = self.get_response(request)

        return response

    def set_notifications(self, schedule):
        dtstart = datetime.combine(schedule.start, datetime.min.time())
        dtstart = timezone.make_aware(dtstart)

        dates = schedule.recurrence.between(dtstart, self.dtend, inc=True,
                                            dtstart=dtstart)
        for date in dates:
            admin = MA.objects.filter(
                recurrence=schedule, date=date.date(),
                administered=True).first()
            if admin is None:
                # TODO: Alert user, cache status until new MA added.
                print('TODO')
