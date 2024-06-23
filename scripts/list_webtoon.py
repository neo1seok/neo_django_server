import json
import shutil

#import pymysql

import pymysql
from neolib import neoutil

from webtoon.models import Webtoon, Portal

import os
import django

# Django 설정을 로드합니다
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
#django.setup()
from neolib import neoutil
def run():
	map_db_info = {
		"host": "192.168.0.17",
		"port": 3306,
		"user": "neo1seok",
		"passwd": "tofhdna1pi",
		"db": "neo_pwinfo",
		"charset": "utf8"
	}
	conn = pymysql.connect(**map_db_info)
	cur = conn.cursor(pymysql.cursors.DictCursor)

	imgdata = json.loads(neoutil.StrFromFile("scripts/rsc/out_img.json"))

	cur.execute("""
			SELECT * 
			FROM neo_pwinfo.portal;""")
	list_map_portal = cur.fetchall()
	# for tmp in list_map_portal:
	# 	del tmp['seq']
	# 	del tmp['prt_uid']
	# 	del tmp['comment']
	# 	Portal.objects.create(**tmp)

#	exit()
	cur.execute("""
		SELECT * 
		FROM neo_pwinfo.webtoon;""")
	list_map = cur.fetchall()
	#Webtoon.objects.all().delete()
	for tmp in list_map:
		title_id = tmp['id']
		tmp['id'] =  tmp['seq']
		del tmp['seq']
		del tmp['wtn_uid']
		tmp['title_id'] = title_id
		if tmp['status'] == 'HIDDEN':
			continue
		data = imgdata.get(title_id)
		if not data:continue
		if os.path.exists(os.path.join("example/rsc",data["src"])):
			_,name = os.path.split(data["src"])
			shutil.copy(os.path.join("example/rsc",data["src"]),os.path.join("static/webtoon_img",name))
			pass
		#del tmp['id']
		prt_uid =  tmp['prt_uid']
		if prt_uid =="prt_1":
			portal = Portal.objects.get(id=1)
		elif prt_uid =="prt_2":
			portal = Portal.objects.get(id=2)
		status = tmp['status']
		if status == "":
			tmp['status'] = "ACTIVATE"
		tmp["portal"] = portal
		del tmp['prt_uid']

		print(tmp)
		#Webtoon.objects.create(**tmp)

	pass