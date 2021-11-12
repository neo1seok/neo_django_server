import json
import os

from jcsg.models import JcsgContents



def run():
	print(JcsgContents.objects)
	JcsgContents.objects.filter(pk__lte=340).update(status= JcsgContents.Status.READ)
	for f in JcsgContents.objects.all():
		print(f.pk, f.status)
		
# break


