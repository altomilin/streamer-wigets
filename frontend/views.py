from django.shortcuts import render, redirect

from frontend.forms import RegisterForm


def index(request):
    context = {
        'title': 'Виджеты от Кекса'
    }
    return render(request, 'frontend/base.html', context)


def login_page(request):
    context = {
        'title': 'Вход'
    }
    return render(request, 'frontend/login.html', context)


def logout(request):
    pass


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        "form": form,
        "title": "Регистрация",
    }
    return render(request, 'frontend/register.html', context)
