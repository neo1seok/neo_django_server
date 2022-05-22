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

from comm.exceptions import CustomFail
from words_puzzle.models import WordsContents
from words_puzzle.words_functions import calc_all_nums, find_words, remove_words

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
		cmd = self.request.POST.get('cmd')
		print("ApiView post", self.request.POST, cmd)
		logger.debug(f"self.request.POST:{self.request.POST}")
		try:

			ret = getattr(self, '_' + cmd)(self.request.POST)
			result.update(ret)
			pass
		except CustomFail as ext:
			print(ext)

			result = {'result': 'FAIL', 'error': str(ext)}
			pass

		return JsonResponse(result)

	def _get_session(self,post):
		search_word = self.request.session.get('search_word')
		ref_words = self.request.session.get('ref_words')
		enable_number = self.request.session.get('enable_number')

		ret = {"ref_words": ref_words,
		       "search_word": search_word, "enable_number": enable_number
		       }
		return ret
	def _input_refword(self, post):
		logger.debug(f"_input_search")
		str_ref_words = post.get("ref_words")

		self.request.session['ref_words'] = str_ref_words
		print(self.request.session)
		ret = {"ref_words":str_ref_words}
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
		ret = {"search_word":search_word,"enable_number":enable_number}
		return ret

	def _candidate(self,post):

		search_word = post.get("search_word")

		search_word = self.request.session.get('search_word')
		ref_words = self.request.session.get('ref_words')
		if not ref_words:
			raise CustomFail("후보단어 설정이 안되었습니다.")

		if not search_word:
			raise CustomFail("검색값 설정이 안되었습니다.")

		words = {}
		for idx, (word, rword) in enumerate(find_words(search_word, ref_words)):
			words[word] = rword
		list_obj = WordsContents.objects.filter(word__in=list(words.keys()))
		candidate ={tmp.word:words[tmp.word] for tmp in list_obj}
		self.request.session["candidate"] = candidate
		ret = {"candidate":candidate}
		return ret

	def _remove_word(self,post):
		ref_words = self.request.session.get('ref_words')
		remove_word = post.get('remove_word')

		ref_words = remove_words(ref_words, remove_word)
		self.request.session['ref_words'] = ref_words
		ret = {"ref_words": ref_words}
		return ret