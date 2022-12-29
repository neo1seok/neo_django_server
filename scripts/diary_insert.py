import json
import os

from attributedict.collections import AttributeDict

from diary.models import DiaryContents

from neolib import neoutil

def run():
	
	result = json.loads(neoutil.StrFromFile("rsc/diary_2022.json"))
	print("start",len(result))
	DiaryContents.objects.all().delete()
	pk =1
	for tmp in result:
		#print(tmp['no'])
		tmp = AttributeDict(tmp)
		tmp['pk'] = pk
		DiaryContents.objects.create(title = tmp.title,text= tmp.text,date_title= tmp.date_title)
		pk +=1
		
