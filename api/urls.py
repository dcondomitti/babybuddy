from django.conf.urls import url, include
from rest_framework import routers

from .views import (BabyViewSet, DiaperChangeViewSet, FeedingViewSet,
                    SleepViewSet, TummyTimeViewSet, UserViewSet)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'babies', BabyViewSet)
router.register(r'diaper-changes', DiaperChangeViewSet)
router.register(r'feedings', FeedingViewSet)
router.register(r'sleep', SleepViewSet)
router.register(r'tummy-times', TummyTimeViewSet)
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
