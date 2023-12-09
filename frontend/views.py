from django.shortcuts import render

def index(request):
    context = {
        'title': 'Виджеты от Кекса'
    }
    return render(request, 'frontend/base.html', context)


def login(request):
    context = {
        'title': 'Вход'
    }
    return render(request, 'frontend/login.html', context)


def logout(request):
    pass


def register(request):
    pass
