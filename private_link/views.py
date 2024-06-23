from django.shortcuts import render
from rest_framework import viewsets, permissions

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from comm.base_class import BaseModelViewSet
# Create your views here.
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication,))
from .models import PrvLink
from .serializers import PrvLinkSerializer


def main_view(request):
	return render(request, 'private.html', {})


class PrivateLinkViewSet(BaseModelViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
#	permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
	queryset = PrvLink.objects.all()
	serializer_class = PrvLinkSerializer
