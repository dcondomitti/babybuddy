# -*- coding: utf-8 -*-
from django import forms

from health import models


class MedicationForm(forms.ModelForm):
    class Meta:
        model = models.Medication
        fields = ['name', 'dose_type', 'notes']


class MedicationRecurrenceForm(forms.ModelForm):
    class Meta:
        model = models.MedicationRecurrence
        fields = ['child', 'medication', 'start', 'time', 'recurrence']
