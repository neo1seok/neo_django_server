import json
import os

from jcsg.models import JcsgContents
from neolib import neoutil
from words_puzzle.models import WordsContents
from words_puzzle.words_functions import calc_all_nums, find_words, remove_words


def run():
	#list_words = [tmp.word for tmp in WordsContents.objects.all()]

	#print(list_words)
	#return
	refchar = '출사중라자모불액취람체례무락하사이더바수행국증이'

	list_inputword = [
		"*늬**",
		"연*행*",
		"*크*늬",
	]

	while True:

		print("refchar:", refchar)

		if len(list_inputword) == 0:
			break

		fword = list_inputword.pop(0)

		enable_words = calc_all_nums(fword, refchar)
		print("enable_words", enable_words)
		list_rword = {}
		lobj=[]
		list_words =[]
		for idx, (word, rword) in enumerate(find_words(fword, refchar)):
			list_words.append(word)
			list_rword[word] = rword

		#if idx % 100 == 99:
		print()
		loword = WordsContents.objects.filter(word__in=list_words)
	#	print(loword)
	#	lobj += loword
	#	print(idx, enable_words)
		list_words = []
		#	continue





		select = {}
		for idx, obj in enumerate(loword):
			select[idx] = list_rword[obj.word]
			print(idx, obj.word)
		print(select)
		while True:
			ridx = input(f"선택 단어: {list(select.keys())}\n")

			try:
				refchar = remove_words(refchar, select[int(ridx)])
				neoutil.StrToFile(refchar, "rsc/lastref.txt")
				break
			except Exception as ext:
				print("잘못 누르셨습니다. \n", ext)

# break


