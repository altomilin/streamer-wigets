from django.shortcuts import render, redirect
from frontend.forms import RegisterForm
from django.contrib import messages
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
    widgets_list = WidgetCounter.objects.filter(user=request.user)
    context = {
        'title': 'Виджеты',
        'widgets_list': widgets_list,
    }
    return render(request, 'frontend/widgets.html', context)


def widgets_detail(request, widget_uuid):
    widget = WidgetCounter.objects.filter(user=request.user, uuid=widget_uuid)[0]

    context = {
        'widget': widget,
    }
    return render(request, 'frontend/widget.html', context)

