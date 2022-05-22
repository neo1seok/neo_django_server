from django.db import models

# Create your models here.
from django.db.models import TextField


class WordsContents(models.Model):

	word = models.CharField(max_length=128, default=None)
	type = models.CharField(max_length=20, default=None)
	description: TextField = models.TextField(default=None,blank=True,null=True)


	def __str__(self):
		return f"{self.word} - {self.type}"
