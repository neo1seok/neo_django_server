from django.urls import path
from . import views
from .views import ApiView

urlpatterns = [
    path('', views.DiaryView.as_view(), name='main'),
    path('<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),

    path('api',views.ApiView.as_view(),name='api')
]