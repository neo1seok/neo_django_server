import logging


from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views import generic
from comm.base_class import BaseView

# MarsMixin 는 공통으로 사용할 view  중요한건 TemplateView 앞에 와야 한다는 거다.
from jcsg.models import JcsgContents
from django.http import HttpResponse, JsonResponse
logger = logging.getLogger(__name__)

class JcsgNovelView(BaseView,generic.ListView):
	template_name = 'jcsg.html'
	context_object_name = 'jcsg_contents'
	model = JcsgContents
	
	
	
	def get_queryset(self):
		print("__name__",__name__)
		logger.debug(f"__name__:{__name__}")
		type = self.request.GET.get('type', 'normal')
		print(self.request, type)

		if type =='all':
			return JcsgContents.objects.all()

		if type =='conv':

			return JcsgContents.objects.filter(
				status=JcsgContents.Status.NOT_READ)[:10]

			#return JcsgContents.objects.all()

		else:
			bf = list(JcsgContents.objects.filter(
				status=JcsgContents.Status.READ))
			logger.debug(f"cur :{bf}")
			cur = list(JcsgContents.objects.filter(
				status=JcsgContents.Status.NOT_READ))
			logger.debug(f"cur :{cur}")
			entry_list = list(cur)
			return bf[-2:] + cur[:10]

		
		# return JcsgContents.objects.filter(
		# 	status=JcsgContents.Status.NOT_READ)

class JcsgNovelDetailView(BaseView,generic.DetailView):
	template_name = 'jcsg_detail.html'
	context_object_name = 'jcsg_content'
	model = JcsgContents

	def get(self, request, *args, **kwargs):
		ret = super().get(request, *args, **kwargs)
		print("JcsgNovelDetailView Get pk",self.kwargs.get('pk'))
		return ret
	
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		print("JcsgNovelDetailView get_context_data pk", self.kwargs)
		
		pk = self.kwargs.get('pk')
		JcsgContents.objects.filter(pk=pk).update(status=JcsgContents.Status.READ)
		#JcsgContents.objects.get(pk).update(status = JcsgContents.Status.READ)


		context['exam'] = 'exam data'
		return context




class ApiView(generic.View):
	def post(self, request):


		#logger.debug(f"pk:{pk} cmd:{cmd}")
		result = {'result': 'OK'}
		try:
			cmd = self.request.POST.get('cmd')
			logger.debug(f"self.request.POST:{self.request.POST}")
			getattr(self,'_'+cmd)(**self.request.POST)
			pass
		except Exception as ext:
			result = {'result': 'FAIL', 'error': str(ext)}
			pass

		return JsonResponse(result)

	def _cancel_read(self,**kwargs):

		pk = kwargs.get('pk')[0]
		logger.debug(f"_cancel_read pk:{pk}")
		JcsgContents.objects.filter(pk=pk).update(status=JcsgContents.Status.NOT_READ)
		ret ={}
		return ret