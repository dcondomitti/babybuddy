# -*- coding: utf-8 -*-
from django.contrib import admin

from health import models


@admin.register(models.Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dose_type', 'notes')
    search_fields = ('name', 'dose_type', 'notes')
    fields = ['name', 'dose_type', 'notes']


@admin.register(models.MedicationAdministration)
class MedicationAdministrationAdmin(admin.ModelAdmin):
    list_display = ('child', 'medication_event', 'date', 'time', 'administered')
    list_filter = ('child', 'medication_event', 'date', 'administered')
    search_fields = ('child__first_name', 'child__last_name')


@admin.register(models.MedicationEvent)
class MedicationEventAdmin(admin.ModelAdmin):
    list_display = ('child', 'medication', 'dose', 'start_date', 'start_time',
                    'recurring', 'recurring_type')
    list_filter = ('child', 'medication', 'recurring')
    search_fields = ('child__first_name', 'child__last_name',
                     'medication__name')
