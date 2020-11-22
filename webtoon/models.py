from django.db import models

# Create your models here.
# Create your models here.
from django.db import models

# Create your models here.


class Portal(models.Model):
	name = models.CharField(max_length=20) #varchar(20)
	search_form = models.CharField(max_length=256) #varchar(256)
	list_webtoon = models.TextField() #text

	contents_webtoon = models.TextField() #text

	main_url = models.CharField(max_length=256) #varchar(256)
	etc = models.TextField() #text

	updt_date = models.DateTimeField(auto_now_add=True)
	reg_date = models.DateTimeField(auto_now=True)


class Webtoon(models.Model):
	prt_uid = models.TextField()  # varchar(20)
	portal = models.ForeignKey(Portal, on_delete=models.CASCADE)
	title = models.CharField(max_length=64)  # varchar(64)
	today_title = models.TextField()  # text
	wid = models.CharField(max_length=32)  # varchar(32)
	lastno = models.CharField(max_length=32)  # varchar(32)
	dates = models.CharField(max_length=32)  # varchar(32)
	status = models.CharField(max_length=20)  # varchar(20)

	updt_date = models.DateTimeField(auto_now_add=True)
	reg_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title