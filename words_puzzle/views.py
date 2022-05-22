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

from words_puzzle.words_functions import calc_all_nums

logger = logging.getLogger(__name__)


def main_view(request):
	return render(request, 'words_puzzle.html', {})


class MainView(BaseView, generic.TemplateView):
	template_name = 'words_puzzle.html'

	def get(self, request, *args, **kwargs):
		ret = super().get(request, *args, **kwargs)
		print("MainView Get pk", self.kwargs.get('pk'))

		return ret

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)


		context['exam'] = 'exam data'
		return context


class ApiView(generic.View):
	def post(self, request):

		# logger.debug(f"pk:{pk} cmd:{cmd}")
		result = {'result': 'OK'}
		#try:
		cmd = self.request.POST.get('cmd')
		print("ApiView post", self.request.POST,cmd)
		logger.debug(f"self.request.POST:{self.request.POST}")
		ret = getattr(self, '_' + cmd)(self.request.POST)
		result.update(ret)
		#	pass
		#except Exception as ext:
		#	print(ext)

		#	result = {'result': 'FAIL', 'error': str(ext)}
		#	pass

		return JsonResponse(result)

	def _input_refword(self, post):
		logger.debug(f"_input_search")
		str_ref_words = post.get("ref_words")

		self.request.session['ref_words'] = str_ref_words
		print(self.request.session)
		ret = {}
		return ret

	def _input_search(self, post):
		print(self.request.session)
		search_word = post.get("search_word")
		ref_words = self.request.session.get('ref_words')
		print('self.request.session',search_word,ref_words)
		logger.debug(f"_input_search")
		enable_number = calc_all_nums(search_word,ref_words)
		self.request.session['search_word'] = search_word
		self.request.session['enable_number'] = enable_number
		ret = {"enable_number":enable_number}
		return ret

