from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response

from comm.base_class import BaseModelViewSet, IsListOrIsAuthenticated
from .filters import WebtoonFilter
from .forms import WebtoonForm
from .models import Webtoon, Portal

from rest_framework import generics, permissions, serializers, viewsets, status

from .serializers import WebtoonSerializer, PortalSerializer


#from rest_framework.decorators import detail_route, list_route

def main_view(request):
	return render(request, 'webtoon.html', {})



class WebtoonCreateView(generic.CreateView):
	template_name = 'webtoon_edit.html'
	context_object_name = 'webtoons'
	success_url = '/' #1
	form_class = WebtoonForm  # 2

class WebtoonListView(generic.ListView):
	template_name = 'webtoon_list.html'
	context_object_name = 'webtoons'
	model = Webtoon


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['exam'] = 'exam data'
		return context


# @method_decorator(name='list', decorator=swagger_auto_schema(
#     operation_description="description from swagger_auto_schema via method_decorator"
# ))
## https://chatgpt.com/share/e12d5a41-b1cd-45b6-8420-3ccd13878fff 를 보고 확인 함.
class PortalViewSet(BaseModelViewSet):
#class WebtoonViewSet(viewsets.ViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
#	permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticatedOrReadOnly]
	queryset = Portal.objects.all()
	serializer_class = PortalSerializer


class WebtoonViewSet(BaseModelViewSet):
#class WebtoonViewSet(viewsets.ViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsListOrIsAuthenticated]
	queryset = Webtoon.objects.all()
	serializer_class = WebtoonSerializer
	filter_backends = (DjangoFilterBackend,)
	filterset_class = WebtoonFilter


	def list(self, request, *args, **kwargs):
		print("request",request)
		print("kwargs",kwargs)
		response = super().list(request, *args, **kwargs)
		print("List Response Data:", response.data)
		return response

	# def list(self, request):
	# 	print("list")
	# 	pass

	# def create(self, request):
	# 	print("create")
	# 	pass
	#
	# def retrieve(self, request, pk=None):
	# 	pass
	#
	# def update(self, request, pk=None):
	# 	pass
	#
	# def partial_update(self, request, pk=None):
	# 	pass

	def destroy(self, request, pk=None):
		pass
	# @action(detail=True,methods=['post'])
	# def get_active_list(self, request, pk=None):
	# 	user = self.get_object()
	# 	serializer = WebtoonSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		user.set_password(serializer.data['password'])
	# 		user.save()
	# 		return Response({'status': 'password set'})
	# 	else:
	# 		return Response(serializer.errors,
	# 		                status=status.HTTP_400_BAD_REQUEST)

	# @action(detail=False)
	# def get_active_list(self, request):
	# 	webtoon = self.get_object()
	# 	status = self.request.query_params.get('status', None)
	#
	# 	page = self.paginate_queryset(recent_users)
	# 	if page is not None:
	# 		serializer = self.get_serializer(page, many=True)
	# 		return self.get_paginated_response(serializer.data)
	#
	# 	serializer = self.get_serializer(recent_users, many=True)
	# 	return Response(serializer.data)


