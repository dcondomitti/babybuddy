# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext_lazy as _


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
    medication_event = models.ForeignKey(
        'MedicationEvent',
        on_delete=models.CASCADE,
        related_name='medication_administration',
        verbose_name=_('Medication event')
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


class MedicationEvent(models.Model):
    model_name = 'medication_event'
    child = models.ForeignKey(
        'core.Child',
        on_delete=models.CASCADE,
        related_name='medication_event',
        verbose_name=_('Child')
    )
    medication = models.ForeignKey(
        'Medication',
        on_delete=models.CASCADE,
        related_name='medication_event',
        verbose_name=_('Medication')
    )
    dose = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name=_('Dose')
    )
    start_date = models.DateField(
        blank=False,
        null=False,
        verbose_name=_('Start date')
    )
    start_time = models.TimeField(
        blank=False,
        null=False,
        verbose_name=_('Start time')
    )
    end_date = models.DateField(
        null=True,
        verbose_name=_('End date')
    )
    end_time = models.TimeField(
        null=True,
        verbose_name=_('End time')
    )
    recurring = models.BooleanField(
        default=False,
        verbose_name=_('Recurring')
    )
    recurring_type = models.CharField(
        blank=True,
        choices=[
            ('hourly', _('Hourly')),
            ('daily', _('Daily')),
            ('weekly', _('Weekly')),
            ('monthly', _('Monthly')),
            ('yearly', _('Yearly')),
        ],
        max_length=255,
        verbose_name=_('Frequency')
    )
    separation_count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Separation')
    )
    max_occurrences = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Max occurrences')
    )
    dow = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Day of week')
    )
    hod = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Hour of day')
    )
    wom = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Week of month')
    )
    dom = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Day of month')
    )
    moy = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Month of year')
    )

    objects = models.Manager()

    class Meta:
        default_permissions = ('view', 'add', 'change', 'delete')
        ordering = ['-start_date', '-start_time']
        verbose_name = _('Medication event')
        verbose_name_plural = _('Medication events')

    def __str__(self):
        return '{} ({})'.format(self.medication.name, self.recurring_type)
