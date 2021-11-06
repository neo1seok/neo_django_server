from django.urls import path
from . import views
from .views import ApiView

urlpatterns = [
    path('', views.JcsgNovelView.as_view(), name='main'),
    path('<int:pk>/', views.JcsgNovelDetailView.as_view(), name='jcsg_detail'),

    path('api',views.ApiView.as_view(),name='api')
]