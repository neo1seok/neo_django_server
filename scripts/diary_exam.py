import json
import os

from jcsg.models import JcsgContents
from neolib import neoutil

def run():
	
	result = json.loads(neoutil.StrFromFile("rsc/diary_2021.json"))
	print("start",len(result))

	for tmp in result:
		print(tmp['title'])

