from django.urls import path
from rest_framework.routers import DefaultRouter

from counter import views
from counter.views import CounterViewSet, WidgetCounterViewSet

router = DefaultRouter()
router.register('counters', CounterViewSet)
router.register('widgets', WidgetCounterViewSet)

urlpatterns = router.urls
