from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    #path('', views.password_list, name='password_list'),
	path('', RedirectView.as_view(url='/password/list'),name='main'),
	path('list/', views.PasswordListView.as_view(), name='password_list'),

	path('idx/', views.IndexView.as_view(), name='password_idx'),


	path('new/', views.PasswordNewView.as_view(), name='password_new'),
	path('<int:pk>/', views.PasswordDetailView.as_view(), name='password_detail'),
    path('<int:pk>/edit/', views.PasswordEditView.as_view(), name='password_edit'),


	path('header/new/', views.PasswordHeaderNewView.as_view(), name='password_header_new'),
	path('header/<int:pk>/', views.PasswordHeaderDetailView.as_view(), name='password_header_detail'),
	path('header/<int:pk>/edit/', views.password_edit, name='password_header_edit'),

]