from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from counter.serializers import CounterSerializer, WidgetCounterSerializer
from counter.models import Counter, WidgetCounter
from counter.permissions import IsOwnerOrReadOnly


def index(request):
    return render(request, "counter/counter.html")


class CounterViewSet(ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @action(methods=['post'], detail=True, url_path='set-value')
    def set_value(self, request, *args, **kwargs):
        counter = self.get_object()
        new_value = int(request.data.get('value', 0))
        serializer = CounterSerializer(counter, data={'value': new_value}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='increase')
    def increase_value(self, request, *args, **kwargs):
        counter = self.get_object()
        new_value = counter.value + int(request.data.get('increase_value', counter.default_increment))
        serializer = CounterSerializer(counter, data={'value': new_value}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='decrease')
    def decrease_value(self, request, *args, **kwargs):
        counter = self.get_object()
        new_value = counter.value - int(request.data.get('decrease_value', counter.default_increment))
        serializer = CounterSerializer(counter, data={'value': new_value}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WidgetCounterViewSet(ModelViewSet):
    queryset = WidgetCounter.objects.all()
    serializer_class = WidgetCounterSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            # You can customize the status code here
            status_code = status.HTTP_200_OK if request.htmx else status.HTTP_204_NO_CONTENT
            return Response(status=status_code)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True, url_path='counter-widget')
    def get_counter_widget(self, request, *args, **kwargs):
        widget = self.get_object()
        print(widget.counters.all())
        context = {
            'widget_data': widget,
        }
        return render(request, 'counter/widget.html', context)
