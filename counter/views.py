from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from counter.serializers import CounterSerializer, WidgetCounterSerializer
from counter.models import Counter, WidgetCounter


def index(request):
    return render(request, "counter/counter.html")


class CounterViewSet(ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer

    @action(methods=['post'], detail=True, url_path='increase')
    def increase_value(self, request, *args, **kwargs):
        counter = self.get_object()
        counter.value += request.data.get('increase_value', counter.default_increment)
        counter.save()
        return HttpResponse(counter)

    @action(methods=['post'], detail=True, url_path='decrease')
    def increase_value(self, request, *args, **kwargs):
        counter = self.get_object()
        counter.value -= request.data.get('decrease_value', counter.default_increment)
        counter.save()
        return HttpResponse(counter)


class WidgetCounterViewSet(ModelViewSet):
    queryset = WidgetCounter.objects.all()
    serializer_class = WidgetCounterSerializer

    @action(methods=['get'], detail=True, url_path='counter-widget')
    def get_counter_widget(self, request, *args, **kwargs):
        widget = self.get_object()
        print(widget.counters.all())
        context = {
            'widget_data': widget,
        }
        return render(request, 'counter/widget.html', context)
