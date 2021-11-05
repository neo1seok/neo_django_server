from django.urls import path
from . import views


urlpatterns = [
    path('', views.JcsgNovelView.as_view(), name='main'),
    path('<int:pk>/', views.JcsgNovelDetailView.as_view(), name='jcsg_detail'),


]