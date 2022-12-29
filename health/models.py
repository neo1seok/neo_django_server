from django.db import models

# Create your models here.

class HealthBp(models.Model):

	sys_bp = models.IntegerField(blank=True,default=None)
	dia_bp = models.IntegerField(blank=True,default=None)
	pulse = models.IntegerField(blank=True,default=None)
	status = models.CharField(max_length=20, default=None)
	param = models.TextField(blank=True,default=None)
	updt_date = models.DateTimeField(auto_now_add=True)
	reg_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.sys_bp


class HealthWeight(models.Model):

	weight = models.FloatField(blank=True,default=None)

	status = models.CharField(max_length=20, default=None)
	param = models.TextField(blank=True, default=None)
	updt_date = models.DateTimeField(auto_now_add=True)
	reg_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.weight
