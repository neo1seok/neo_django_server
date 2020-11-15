from django.urls import path
from . import views


urlpatterns = [
    #path('', views.password_list, name='password_list'),
	path('', views.PasswordListView.as_view(), name='password_list'),

	path('idx/', views.IndexView.as_view(), name='password_idx'),
	path('new/', views.password_new, name='password_new'),

    #path('<int:pk>/', views.password_detail, name='password_detail'),
	path('<int:pk>/', views.PasswordDetailView.as_view(), name='password_detail'),


    # path('post/new', views.password_new, name='password_new'),
    path('<int:pk>/edit/', views.password_edit, name='password_edit'),
	path('<int:pk>/edit_header/', views.password_edit, name='password_edit_header'),
]