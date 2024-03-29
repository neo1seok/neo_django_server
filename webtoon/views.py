from django.shortcuts import render

# Create your views here.
from django.views import generic

from .forms import WebtoonForm
from .models import Webtoon

from rest_framework import generics, permissions, serializers,viewsets

from .serializers import WebtoonSerializer


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



class WebtoonViewSet(viewsets.ModelViewSet):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [permissions.IsAdminUser,permissions.IsAuthenticated]
	queryset = Webtoon.objects.all()
	serializer_class = WebtoonSerializer
