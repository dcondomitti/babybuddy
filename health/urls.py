# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'health'

urlpatterns = [
    path(
        'medications/',
        views.MedicationList.as_view(),
        name='medication-list'
    ),
    path(
        'medications/add/',
        views.MedicationAdd.as_view(),
        name='medication-add'
    ),
    path(
        'medications/<int:pk>/',
        views.MedicationUpdate.as_view(),
        name='medication-update'
    ),
    path(
        'medications/<int:pk>/delete/',
        views.MedicationDelete.as_view(),
        name='medication-delete'
    ),
]
