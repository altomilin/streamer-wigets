from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import render
from counter.serializers import CounterSerializer, WidgetCounterSerializer
from counter.models import WidgetCounter


def create_widget(request):
    if request.method == 'POST':
        widget = WidgetCounterSerializer(
            context={'request': request},
            data=request.POST,
        )

        if widget.is_valid(raise_exception=False):
            widget_obj = widget.save()
            return render(request, 'htmx_frontend/widget.html', {'widget': widget_obj})
        else:
            return Response(widget.errors, status=400)


def widgets(request):
    widgets_list = WidgetCounter.objects.filter(user=request.user)
    return render(request,
                  'htmx_frontend/htmx_widgets.html',
                  {
                      'title': 'HTMX Widgets',
                      'widgets_list': widgets_list,
                  })


def htmx_counter(request):
    if request.method == 'POST':
        counter = CounterSerializer(
            context={'request': request},
            data=request.POST,
        )

        if counter.is_valid(raise_exception=False):
            counter_obj = counter.save()
            return render(request, 'htmx_frontend/counter.html', {'counter': counter_obj})
        return Response(counter.errors, status=400)
    return Response(status=400)


