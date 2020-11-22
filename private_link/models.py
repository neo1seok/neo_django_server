from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class PrvLink(models.Model):
	title = models.CharField(max_length=64)
	link = models.TextField()
	status = models.CharField(max_length=20)

	updt_date = models.DateTimeField(auto_now_add=True)
	reg_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title