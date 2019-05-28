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
    list_display = ('child', 'date', 'time', 'administered')
    list_filter = ('child', 'date', 'administered')
    search_fields = ('child__first_name', 'child__last_name')


@admin.register(models.MedicationRecurrence)
class MedicationRecurrenceAdmin(admin.ModelAdmin):
    list_display = ('child', 'medication')
    list_filter = ('child', 'medication')
