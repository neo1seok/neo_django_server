import json
import os

from diary.models import DiaryContents

DiaryContents
from neolib import neoutil

def run():
	
	result = json.loads(neoutil.StrFromFile("rsc/diary_2021.json"))
	print("start",len(result))

	for tmp in result:
		print(tmp['title'])

