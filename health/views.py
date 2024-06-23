from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from comm.base_class import BaseModelViewSet
# Create your views here.
from .models import HealthBp,HealthWeight
from .serializers import HealthBpSerializer,HealthWeightSerializer


def main_view(request):
	return render(request, 'main.html', {})


class HealthBpViewSet(BaseModelViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	#permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
	queryset = HealthBp.objects.all()
	serializer_class = HealthBpSerializer

	@action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny])
	def recent_data(self, request):
		serializer = self.get_object()
		return Response(serializer.data)


class HealthWeightViewSet(BaseModelViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	#permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
	queryset = HealthWeight.objects.all()
	serializer_class = HealthWeightSerializer

	@action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny])
	def recent_data(self, request):
		serializer = self.get_object()
		return Response(serializer.data)
