
from itertools import permutations
from neolib import neoutil
from collections import Counter


def parse_fmt(fmt):
	print(fmt)
	count = Counter(list(fmt))
	print(count)
	size  = count["*"]
	fmt = fmt.replace("*","{}")
	return fmt,size

def remove_words(refwords,remove_words):
	listrefwords = list(refwords)
	print(refwords)
	for tmp in remove_words:

		idx = listrefwords.index(tmp)
		del listrefwords[idx]
		print(listrefwords,idx,tmp)
	return "".join(listrefwords)

def calc_all_nums(fmt,refwords):
	import math
	fmt, word_size = parse_fmt(fmt)
	return math.factorial(len(refwords))//math.factorial(len(refwords)-word_size)


def find_words(fmt,refwords):
	fmt , word_size = parse_fmt(fmt)
	word_set=set()
	for idx,val in enumerate(permutations(refwords,word_size)):
		val =list(val) +["","","","","","",""]

		fword =fmt.format(*val)
		if fword in word_set: continue
		word_set.add(fword)
		yield  fword,"".join(val[:word_size])
		# if fword in list_words:
		# 	yield fword,"".join(val[:word_size])
			#print(idx,fword)
		#fd  = df[df["word"] == word ]
		# if not fd.size:
		#     is_not_in_word.add(word)
		#     #print(word)
		# else:
		#     is_in_word.add(word)
def exam():
	parse_fmt("**석")

	refchar = input("가능단어를 입력하세요..:\n")
	list_inputword = []
	if not refchar.strip():
		refchar = neoutil.StrFromFile("rsc/lastref.txt")
		refchar = refchar.strip()

		inputword = neoutil.StrFromFile("rsc/input.txt")
		inputword = inputword.replace("\r","")
		list_inputword = inputword.split("\n")

	while True:

		print("refchar:", refchar)
		fword = input("찾을 단어를 입력하세요  예)***거:\n")
		if not fword.strip():
			if len(list_inputword) ==0:
				continue

			fword = list_inputword.pop(0)

		enable_words = calc_all_nums(fword,refchar)
		print("enable_words",enable_words)
		list_rword = {}
		for idx,(word,rword) in 	enumerate(find_words(fword,refchar)):
			if idx % 100 ==0:
				print(idx,enable_words)

			if word in list_words:
				list_rword[word] = rword

		select ={}
		for idx,(word,rword) in enumerate(list_rword.items()):
			select[idx] = rword
			print(idx,word)
		print(list_rword)
		while True :
			ridx = input(f"선택 단어: {list(select.keys())}\n")
			refchar = remove_words(refchar, select[int(ridx)])
			try:

				neoutil.StrToFile(refchar, "rsc/lastref.txt")
				break
			except Exception as ext:
				print("잘못 누르셨습니다. \n",ext)

#pprint(fd)

print()