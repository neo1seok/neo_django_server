from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views import generic
from comm.base_class import BaseView

# MarsMixin 는 공통으로 사용할 view  중요한건 TemplateView 앞에 와야 한다는 거다.
from jcsg.models import JcsgContents


class JcsgNovelView(BaseView,generic.ListView):
	template_name = 'jcsg.html'
	context_object_name = 'jcsg_contents'
	model = JcsgContents
	
	
	
	def get_queryset(self):
		
		type = self.request.GET.get('type', 'normal')
		print(self.request, type)
		return JcsgContents.objects.all() if type == 'all' else JcsgContents.objects.filter(
			status=JcsgContents.Status.NOT_READ)
		
		# return JcsgContents.objects.filter(
		# 	status=JcsgContents.Status.NOT_READ)

class JcsgNovelDetailView(BaseView,generic.DetailView):
	template_name = 'jcsg_detail.html'
	context_object_name = 'jcsg_content'
	model = JcsgContents

	def get(self, request, *args, **kwargs):
		ret = super().get(request, *args, **kwargs)
		print("JcsgNovelDetailView Get")
		return ret
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['exam'] = 'exam data'
		return context
