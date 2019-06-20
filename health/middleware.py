# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils import timezone

from health.models import MedicationAdministration as MA
from health.models import MedicationRecurrence as MR


class MedicationNotificationsMiddleware(object):
    """Add "medication_notifications" context data to the template response.
    This data will be used to set frontend notifications for the user about due
    (and past due) medications based on MedicationRecurrent and
    MedicationAdministration objects."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.dtend = timezone.localtime()
        self.notifications = []

        response = self.get_response(request)

        return response

    def process_template_response(self, request, response):
        # TODO: Cache the results of this process and bust on new MA objects.
        schedules = MR.objects.filter(complete=False).filter(
            start__lte=timezone.localdate())

        for schedule in schedules:
            self.set_notifications(schedule)

        response.context_data['medication_notifications'] = self.notifications

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
                self.notifications.append([schedule, date])
