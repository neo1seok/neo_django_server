from django.urls import path
from . import views


urlpatterns = [
    path('', views.WebtoonListView.as_view(), name='main'),

    path('new/', views.WebtoonCreateView.as_view(), name='webtoon_new'),


]