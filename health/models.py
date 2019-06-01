# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _

from recurrence.fields import RecurrenceField


class Medication(models.Model):
    model_name = 'medication'
    name = models.CharField(
        max_length=255,
        verbose_name=_('Name')
    )
    dose_type = models.CharField(
        help_text=_('Pill, shot, ml, mg, etc.'),
        max_length=255,
        verbose_name=_('Dose type')
    )
    notes = models.TextField(
        blank=True,
        verbose_name=_('Notes')
    )

    objects = models.Manager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        ordering = ['name']
        verbose_name = _('Medication')
        verbose_name_plural = _('Medications')

    def __str__(self):
        return '{}'.format(self.name)


class MedicationAdministration(models.Model):
    model_name = 'medication_administration'
    child = models.ForeignKey(
        'core.Child',
        on_delete=models.CASCADE,
        related_name='medication_administration',
        verbose_name=_('Child')
    )
    administered = models.BooleanField(
        default=True,
        verbose_name=_('Administered')
    )
    date = models.DateField(
        blank=False,
        null=False,
        verbose_name=_('Date')
    )
    time = models.TimeField(
        blank=False,
        null=False,
        verbose_name=_('Time')
    )

    objects = models.Manager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        ordering = ['-date', '-time']
        verbose_name = _('Medication administration')
        verbose_name_plural = _('Medication administrations')

    def __str__(self):
        return str(_('Medication administration'))


class MedicationRecurrence(models.Model):
    model_name = 'medication_recurrence'
    child = models.ForeignKey(
        'core.Child',
        on_delete=models.CASCADE,
        related_name='medication_recurrence',
        verbose_name=_('Child')
    )
    medication = models.ForeignKey(
        'Medication',
        on_delete=models.CASCADE,
        related_name='medication_recurrence',
        verbose_name=_('Medication')
    )
    recurrence = RecurrenceField(
        verbose_name=_('Schedule')
    )

    objects = models.Manager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        verbose_name = _('Medication recurrence')
        verbose_name_plural = _('Medication recurrence')

    def __str__(self):
        return str(_('Medication recurrence'))
