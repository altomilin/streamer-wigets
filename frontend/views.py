from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response

from counter.serializers import WidgetCounterSerializer
from frontend.forms import RegisterForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from counter.models import WidgetCounter, Counter


def index(request):
    context = {
        'title': 'Виджеты от Кекса'
    }
    return render(request, 'frontend/base.html', context)


def login_page(request):
    context = {
        'title': 'Вход'
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = bool(request.POST.get('remember-me', 1))

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Неверная пара логин/пароль')

    return render(request, 'frontend/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"Аккаунт успешно создан для пользователя {user}")
            return redirect('login')

    context = {
        "form": form,
        "title": "Регистрация",
    }
    return render(request, 'frontend/register.html', context)


def widgets(request):
    if not request.user.is_authenticated:
        return redirect('login')
    widgets_list = WidgetCounter.objects.filter(user=request.user)
    context = {
        'title': 'Виджеты',
        'widgets_list': widgets_list,
    }
    return render(request, 'frontend/widgets.html', context)


def widgets_detail(request, widget_uuid):
    widget = WidgetCounter.objects.filter(user=request.user, uuid=widget_uuid)[0]
    url = request.build_absolute_uri(reverse('widget_detail_obs', args=(widget.uuid, )))
    context = {
        'widget': widget,
        'url': url,
    }
    return render(request, 'frontend/widget.html', context)


def widget_data(request, widget_uuid):
    widget = WidgetCounter.objects.filter(uuid=widget_uuid)[0]
    serializer = WidgetCounterSerializer(instance=widget, many=True)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def widget_detail_obs(request, widget_uuid):
    widget = WidgetCounter.objects.filter(uuid=widget_uuid)[0]
    url = request.build_absolute_uri(reverse('widgetcounter-detail', args=(widget.id, )))

    context = {
        'counters': widget.counters.all(),
        'url': url,
    }
    return render(request, 'frontend/obs.html', context)
