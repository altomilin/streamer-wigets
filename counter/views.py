from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from counter.serializers import CounterSerializer, WidgetCounterSerializer
from counter.models import Counter, WidgetCounter


def index(request):
    return render(request, "counter/counter.html")


class CounterViewSet(ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer


class WidgetCounterViewSet(ModelViewSet):
    queryset = WidgetCounter.objects.all()
    serializer_class = WidgetCounterSerializer
