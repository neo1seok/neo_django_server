from django.shortcuts import render

# Create your views here.
from comm.base_class import BaseView

import logging


from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.views import generic
from comm.base_class import BaseView



from django.http import HttpResponse, JsonResponse
logger = logging.getLogger(__name__)


def main_view(request):
	return render(request, 'words_puzzle.html', {})


class MainView(BaseView, generic.TemplateView):
	template_name = 'words_puzzle.html'

	def get(self, request, *args, **kwargs):
		ret = super().get(request, *args, **kwargs)
		print("MainView Get pk", self.kwargs.get('pk'))

		return ret

	# def get_context_data(self, **kwargs):
	# 	# Call the base implementation first to get a context
	# 	context = super().get_context_data(**kwargs)
	# 	# Add in a QuerySet of all the books
	# 	print("MainView get_context_data pk", self.kwargs)
	#
	# 	pk = self.kwargs.get('pk')
	# 	JcsgContents.objects.filter(pk=pk).update(status=JcsgContents.Status.READ)
	# 	# JcsgContents.objects.get(pk).update(status = JcsgContents.Status.READ)
	#
	# 	context['exam'] = 'exam data'
	# 	return context


class ApiView(generic.View):
	def post(self, request):

		# logger.debug(f"pk:{pk} cmd:{cmd}")
		result = {'result': 'OK'}
		try:
			cmd = self.request.POST.get('cmd')
			logger.debug(f"self.request.POST:{self.request.POST}")
			getattr(self, '_' + cmd)(**self.request.POST)
			pass
		except Exception as ext:
			result = {'result': 'FAIL', 'error': str(ext)}
			pass

		return JsonResponse(result)

	# def _cancel_read(self, **kwargs):
	#
	# 	pk = kwargs.get('pk')[0]
	# 	logger.debug(f"_cancel_read pk:{pk}")
	# 	JcsgContents.objects.filter(pk=pk).update(status=JcsgContents.Status.NOT_READ)
	# 	ret = {}
	# 	return ret