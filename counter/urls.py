from django.urls import path
from counter import views

urlpatterns = [
    path('', views.index, name='counter_main_page')
]