import json
import os


from words_puzzle.models import WordsContents
from neolib import neoutil

def run():
	
	result = json.loads(neoutil.StrFromFile("rsc/kr_korean.json"))
	print("start",len(result))
	WordsContents.objects.all().delete()
	pk =1
	for tmp in result:
		tmp['pk'] = pk
		WordsContents.objects.create(**tmp)
		pk +=1
		if (pk% 100)==0:
			print(pk)
		
