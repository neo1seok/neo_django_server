from django.shortcuts import render
from rest_framework import viewsets, permissions

# Create your views here.
from .models import HealthBp,HealthWeight
from .serializers import HealthBpSerializer,HealthWeightSerializer


def main_view(request):
	return render(request, 'main.html', {})


class HealthBpViewSet(viewsets.ModelViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
	queryset = HealthBp.objects.all()
	serializer_class = HealthBpSerializer


class HealthWeightViewSet(viewsets.ModelViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
	queryset = HealthWeight.objects.all()
	serializer_class = HealthWeightSerializer
