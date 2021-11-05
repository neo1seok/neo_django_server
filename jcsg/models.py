from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class JcsgContents(models.Model):
	class Status(models.TextChoices):
		READ = 'READ', _('Read')
		NOT_READ = 'NOT_READ', _('not read')
	
	no = models.CharField(max_length=20,default=None)
	title = models.CharField(max_length=128, default=None)
	contents = models.TextField( default=None)
	
	date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20,  choices=Status.choices,default=Status.NOT_READ)

	updt_date = models.DateTimeField(auto_now_add=True)
	reg_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return f"{self.no} 화 - {self.title}"
