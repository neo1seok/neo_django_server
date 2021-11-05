import json
import os

from jcsg.models import JcsgContents
from neolib import neoutil

def run():
	
	result = json.loads(neoutil.StrFromFile("rsc/result.json"))
	print("start",len(result))
	JcsgContents.objects.all().delete()
	pk =1
	for tmp in result:
		print(tmp['no'])
		tmp['pk'] = pk
		JcsgContents.objects.create(**tmp)
		pk +=1
		
	result = json.loads(neoutil.StrFromFile("rsc/result_spinoff.json"))
	print("start",len(result))
	#JcsgContents.objects.all().delete()
	
	for tmp in result:
		no = tmp['no']
		print(no)
		tmp['pk'] = pk
		tmp['no'] = f"외전 {no}"
		JcsgContents.objects.create(**tmp)
		pk +=1
