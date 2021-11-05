import json
import os

from jcsg.models import JcsgContents
from neolib import neoutil


def run():
	print(JcsgContents.objects)
	JcsgContents.objects.filter(pk__lt=260).update(status= JcsgContents.Status.READ)
	for f in JcsgContents.objects.all():
		print(f.pk, f.status)
		
# break


