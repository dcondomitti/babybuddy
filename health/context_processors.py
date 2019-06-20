# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils import timezone

from health.models import MedicationAdministration as MA
from health.models import MedicationRecurrence as MR


# TODO: Cache this information and bust on MA add.
def medication_notifications(request):
    """Add "medication_notifications" context data to the template response.
    This data will be used to set frontend notifications for the user about due
    (and past due) medications based on MedicationRecurrent and
    MedicationAdministration objects."""
    dtend = timezone.localtime()
    notifications = []

    schedules = MR.objects.filter(complete=False).filter(
        start__lte=timezone.localdate())

    for schedule in schedules:
        dtstart = datetime.combine(schedule.start, datetime.min.time())
        dtstart = timezone.make_aware(dtstart)

        dates = schedule.recurrence.between(dtstart, dtend, inc=True,
                                            dtstart=dtstart)
        for date in dates:
            admin = MA.objects.filter(
                recurrence=schedule, date=date.date(),
                administered=True).first()
            if admin is None:
                notifications.append([schedule, date])

    return {'medication_notifications': notifications}
