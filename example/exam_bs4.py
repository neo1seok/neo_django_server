import os

from bs4 import BeautifulSoup
from neolib import neoutil
from urllib.parse import urlparse, parse_qs
import urllib
soup = BeautifulSoup(neoutil.StrFromFile("rsc/요일전체 _ 네이버 웹툰.html"),"html.parser")
out_result ={}
for tmp in soup.find_all('li',class_='DailyListItem__item--LP6_T'):
	print(tmp)
	title = tmp.find(class_='DailyListItem__info_area--aS5RC').text
	a = tmp.find("a")
	href = a.attrs['href']
	parsed_url = urlparse(href)
	query_params = parse_qs(parsed_url.query)
	titleId = query_params['titleId'][0]

	print(parsed_url,query_params,titleId)

	img = tmp.find("img")
	src = img.attrs['src']


	print(img.attrs['src'])
	print(os.path.exists(os.path.join("rsc",src)))
	data = b''
	with open(os.path.join("rsc",src),'rb') as fi:
		data = fi.read()
	out_result[titleId] = dict(wid=titleId, src=src, title=title,data=data.hex())
	"https://image-comic.pstatic.net/webtoon/818351/thumbnail"+img.attrs['src']
neoutil.StrToFile(neoutil.json_pretty(out_result), "rsc/out/out_img.json")