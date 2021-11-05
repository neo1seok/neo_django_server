import json
import os

from jcsg.models import JcsgContents
from neolib import neoutil

def run():
	
	
	for f in JcsgContents.objects.all():
		print(f.pk, f.status)
# break


