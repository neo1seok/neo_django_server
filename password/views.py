from django.shortcuts import render
from django.shortcuts import render
from django.urls import resolve
from django.utils import timezone
from django.views import generic
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from comm.base_class import BaseModelViewSet
from comm.function import exam_function
from .forms import PasswordForm
from .models import Password, PasswordHeader
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

#from django.core.urlresolvers import resolve
from .serializers import PasswordSerializer, PasswordHeaderSerializer


def appname(request):
	return {'appname': resolve(request.path).app_name}

# Create your views here.
def password_list(request):
	exam = exam_function()
	passwords = Password.objects.filter(updt_date__lte=timezone.now()).order_by('updt_date')
	print('resolve(request.path)',request.resolver_match)

	return render(request, 'password_list.html', {'passwords': passwords,'exam':exam,'title':resolve(request.path).app_name})



class PasswordListView(generic.ListView):
	template_name = 'password_list.html'
	context_object_name = 'passwords'
	model = Password


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['exam'] = 'exam data'
		return context

def password_new(request):
	if request.method == "POST":
		form = PasswordForm(request.POST)
		if form.is_valid():
			password = form.save(commit=False)
			password.author = request.user
			password.published_date = timezone.now()
			password.save()
			return redirect('password:password_detail', pk=password.pk)
	else:
		form = PasswordForm()
	return render(request, 'password_edit.html', {'form': form})



def password_edit(request, pk):
	password = get_object_or_404(Password, pk=pk)
	if request.method == "POST":
		form = PasswordForm(request.POST, instance=password)
		if form.is_valid():
			password = form.save(commit=False)
#			post.author = request.user
#			post.published_date = timezone.now()
			password.save()
			return redirect('password_detail', pk=password.pk)
	else:
		form = PasswordForm(instance=password)
	return render(request, 'password_edit.html', {'form': form})

class PasswordNewView(generic.CreateView):
	template_name = 'password_edit.html'
	context_object_name = 'password'
	model = Password
	fields = ('pheader','site', 'ptail','site_id','etc')


class PasswordEditView(generic.UpdateView):
	template_name = 'password_edit.html'
	context_object_name = 'password'
	model = Password
	fields = ('pheader','site', 'ptail','site_id','etc')


class PasswordDetailView(generic.DetailView):
	template_name = 'password_detail.html'
	context_object_name = 'password'
	model = Password


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['exam'] = 'exam data'
		return context


class PasswordHeaderNewView(generic.CreateView):
	template_name = 'password_edit.html'
	context_object_name = 'password_header'
	model = PasswordHeader
	fields = ('title','hint', 'special_letter','etc')


class PasswordHeaderEditView(generic.UpdateView):
	template_name = 'password_edit.html'
	context_object_name = 'password_header'
	model = PasswordHeader
	fields = ('title','hint', 'special_letter','etc')

class PasswordHeaderDetailView(generic.DetailView):
	template_name = 'password_header_detail.html'
	context_object_name = 'password_header'
	model = PasswordHeader


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['exam'] = 'exam data'
		return context


#
# def password_detail(request, pk):
# 	password = get_object_or_404(Password, pk=pk)
# 	return render(request, 'password_detail.html', {'password': password})
#

class PasswordViewSet(BaseModelViewSet):
	queryset = Password.objects.all()
	serializer_class = PasswordSerializer


class PasswordHeaderViewSet(BaseModelViewSet):
	queryset = PasswordHeader.objects.all()
	serializer_class = PasswordHeaderSerializer

class IndexView(generic.ListView):
	template_name = 'index.html'
	model = Password
	context_object_name = 'passwords'


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['exam_data'] = 'exam data'
		return context