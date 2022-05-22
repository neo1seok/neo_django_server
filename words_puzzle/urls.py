from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.MainView.as_view(), name='main'),
#     path('api',views.ApiView.as_view(),name='api')
# ]

urlpatterns = [
    path('', views.main_view, name='main'),


]