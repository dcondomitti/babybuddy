# -*- coding: utf-8 -*-
from django.urls import reverse_lazy

from babybuddy.mixins import PermissionRequired403Mixin
from babybuddy.views import BabyBuddyFilterView
from core.views import CoreAddView, CoreDeleteView, CoreUpdateView
from health import forms, models


class MedicationList(PermissionRequired403Mixin, BabyBuddyFilterView):
    model = models.Medication
    template_name = 'health/medication_list.html'
    permission_required = ('health.view_medication',)
    paginate_by = 10
    filterset_fields = ('name', 'dose_type')


class MedicationAdd(CoreAddView):
    model = models.Medication
    permission_required = ('health.add_medication',)
    form_class = forms.MedicationForm
    success_url = reverse_lazy('health:medication-list')


class MedicationUpdate(CoreUpdateView):
    model = models.Medication
    permission_required = ('health.change_medication',)
    fields = ['name', 'dose_type', 'notes']
    success_url = reverse_lazy('health:medication-list')


class MedicationDelete(CoreDeleteView):
    model = models.Medication
    permission_required = ('health.delete_medication',)
    success_url = reverse_lazy('health:medication-list')


class MedicationRecurrenceList(PermissionRequired403Mixin,
                               BabyBuddyFilterView):
    model = models.MedicationRecurrence
    template_name = 'health/medicationrecurrence_list.html'
    permission_required = ('health.view_medication_recurrence',)
    paginate_by = 10
    filterset_fields = ('child', 'medication')


class MedicationRecurrenceAdd(CoreAddView):
    model = models.MedicationRecurrence
    permission_required = ('health.add_medication_recurrence',)
    form_class = forms.MedicationRecurrenceForm
    success_url = reverse_lazy('health:medication_recurrence-list')


class MedicationRecurrenceUpdate(CoreUpdateView):
    model = models.MedicationRecurrence
    permission_required = ('health.change_medication_recurrence',)
    fields = ['child', 'medication', 'start', 'time', 'recurrence']
    success_url = reverse_lazy('health:medication_recurrence-list')


class MedicationRecurrenceDelete(CoreDeleteView):
    model = models.MedicationRecurrence
    permission_required = ('health.delete_medication_recurrence',)
    success_url = reverse_lazy('health:medication_recurrence-list')
