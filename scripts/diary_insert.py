import datetime
import json
import os

from diary.models import DiaryContents
from neolib import neoutil

def run():
	
	result = json.loads(neoutil.StrFromFile("rsc/diary_2021.json"))
	print("start",len(result))
	DiaryContents.objects.all().delete()
	pk =1
	for tmp in result:
		#print(tmp['no'])
		del tmp['uid'],tmp['summary'],tmp['date']
		tmp['pk'] = pk
		#date = tmp['date']
		#date = datetime.datetime.strptime(date,"%Y-%m-%d")
		#print(date)
		DiaryContents.objects.create(**tmp)
		pk +=1
		
