import json
import os

from jcsg.models import JcsgContents
from neolib import neoutil
from words_puzzle.models import WordsContents
def run():
	
	for f in WordsContents.objects.all():
		print(f, f.word)
# break


