from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('main_pw/', views.main_password_list, name='main_pw'),

]