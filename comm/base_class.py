from rest_framework.pagination import PageNumberPagination

import neo_django_server
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import permissions
from django.conf import settings


class BaseView(object):
	time_on_mars = 5

	def get_time_on_mars(self):
		"""
		Does what it takes to return a time on mars be it calculation
		or returning a property set on the object. Should return a property
		from the object if it is a constant. Should calcualte in the method
		if it is going to be dynanic
		"""
		return self.time_on_mars

	def get_context_data(self, **kwargs):
		context = super(BaseView, self).get_context_data(**kwargs)
		context['time_on_mars'] = self.get_time_on_mars()
		context['version'] = neo_django_server.__version__

		return context



class IsAdminOrAuthenticated(permissions.BasePermission):
	def has_permission(self, request, view):
		if settings.DEBUG:
			return True
		# 관리자는 항상 접근을 허용
		if request.user and request.user.is_staff:
			return True
		# 인증된 사용자에게 접근을 허용
		return request.user and request.user.is_authenticated
class IsListOrIsAuthenticated(permissions.BasePermission):
	"""
	Custom permission to allow anyone to access the list view,
	but require authentication for other actions.
	"""
	def has_permission(self, request, view):
		# Check if the action is 'list'
		if view.action == 'list':
			return True
		if settings.DEBUG:
			return True
		# 관리자는 항상 접근을 허용

		if request.user and request.user.is_staff:
			return True

		# For other actions, check if the user is authenticated
		return request.user and request.user.is_authenticated

class BasePagination(PageNumberPagination):
	page_size = 5  # 페이지 당 객체 수
	page_size_query_param = 'page_size'
	max_page_size = 100

class BaseModelViewSet(viewsets.ModelViewSet):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAdminOrAuthenticated]
	pagination_class = BasePagination