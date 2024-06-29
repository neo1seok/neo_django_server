import json

#import pymysql

import pymysql
from attributedict.collections import AttributeDict
from neolib import neoutil

from password.models import Password,PasswordHeader

import os
import django

# Django 설정을 로드합니다
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
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
			SELECT seq, pwd_uid, phd_uid, site, ptail, id, etc, status, updt_date, reg_date, comment 
FROM neo_pwinfo.passwd;
;""")
	list_map_passwd = cur.fetchall()
	# for tmp in list_map_portal:
	# 	del tmp['seq']
	# 	del tmp['prt_uid']
	# 	del tmp['comment']
	# 	Portal.objects.create(**tmp)

#	exit()
	cur.execute("""
		SELECT seq, phd_uid, title, hint, special_letter, etc, updt_date, reg_date, comment 
FROM neo_pwinfo.pheader;
;""")
	list_map_phd = cur.fetchall()
	dict_phd = { }
	PasswordHeader.objects.all().delete()
	Password.objects.all().delete()
	for id,phd in enumerate(list_map_phd):
		phd = AttributeDict(phd)
		args = phd.copy()
		print(args)
		args['id'] = id+1
		del args['phd_uid']
		del args['seq']

		res =PasswordHeader.objects.create(**args)
		print("res",res.id)
		dict_phd[phd.phd_uid] = res.id
		pass

	for id,pwd in enumerate(list_map_passwd,1):
		pwd = AttributeDict(pwd)
		print(pwd)
		if not pwd.phd_uid: continue
		args = pwd.copy()


		phd_id = dict_phd[pwd.phd_uid]
		print(phd_id)
		pheader = PasswordHeader.objects.get(id=phd_id)
		#pheader = PasswordHeader.objects.get(phd_id)
		args['pheader'] = pheader

		args['site_id'] = args['id']
		args['id'] = id
		del args['phd_uid']
		del args['seq']
		del args['pwd_uid']


		print(args)
		res = Password.objects.create(**args)
		pass

	pass