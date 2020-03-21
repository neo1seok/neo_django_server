from django.urls import path
from . import views


urlpatterns = [
    path('', views.password_list, name='password_list'),
	path('password/new', views.password_new, name='password_new'),
    path('password/<int:pk>/', views.password_detail, name='password_detail'),
    # path('post/new', views.password_new, name='password_new'),
    path('password/<int:pk>/edit/', views.password_edit, name='password_edit'),
]