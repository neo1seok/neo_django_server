from django.db import models
from django.utils import timezone
# Create your models here.


class PasswordHeader(models.Model):
	title = models.CharField(max_length=20)
	hint = models.TextField(blank=True)
	special_letter = models.CharField(max_length=5)
	etc = models.TextField(blank=True)
	updt_date = models.DateTimeField(auto_now_add=True)
	reg_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class Password(models.Model):
	pheader = models.ForeignKey(PasswordHeader, on_delete=models.CASCADE)
	site = models.CharField(max_length=64)
	ptail = models.CharField(max_length=64)
	site_id = models.CharField(max_length=64,blank=True)
	etc = models.TextField(blank=True)
	status = models.CharField(max_length=20,blank=True,null=True)
	updt_date = models.DateTimeField(auto_now_add=True)
	reg_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.site

