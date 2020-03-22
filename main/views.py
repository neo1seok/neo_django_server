from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from comm.function import exam_function
from password.models import Password


def main_view(request):
	return render(request, 'main.html', {})
# Create your views here.

def main_password_list(request):
	exam = exam_function()
	passwords = Password.objects.filter(updt_date__lte=timezone.now()).order_by('updt_date')
	print('resolve(request.path)',request.resolver_match)

	return render(request, 'main_pw.html', {'passwords': passwords,'exam':exam})
