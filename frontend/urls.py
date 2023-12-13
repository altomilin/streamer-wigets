from django.urls import path, include

from frontend import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('widgets', views.widgets, name='widgets'),
    path('widgets/<uuid:widget_uuid>', views.widget_data, name='widget_data'),
    path('widgets_detail/<uuid:widget_uuid>', views.widgets_detail, name='widgets_detail'),
    path('counter/<uuid:widget_uuid>', views.widget_detail_obs, name='widget_detail_obs')
]