from django.urls import path, include

import htmx_frontend.views as views


urlpatterns = [
    path('main-widgets/', views.widgets, name='widgets_main'),
    path('create-widget/', views.create_widget, name='create_widget'),
    path('htmx-counter/', views.htmx_counter, name='htmx_counter'),
]