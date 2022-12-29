
#import pymysql

import pymysql
from neolib import neoutil

from webtoon.models import Webtoon, Portal


def run():
	map_db_info = {
		"host": "192.168.219.17",
		"port": 3306,
		"user": "neo1seok",
		"passwd": "tofhdna1pi",
		"db": "neo_pwinfo",
		"charset": "utf8"
	}
	conn = pymysql.connect(**map_db_info)
	cur = conn.cursor(pymysql.cursors.DictCursor)

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
	Webtoon.objects.all().delete()
	for tmp in list_map:
		tmp['id'] =  tmp['seq']
		del tmp['seq']
		del tmp['wtn_uid']
		tmp['wid'] = tmp['id']
		#del tmp['id']
		prt_uid =  tmp['prt_uid']
		if prt_uid =="prt_1":
			portal = Portal.objects.get(id=1)
		elif prt_uid =="prt_2":
			portal = Portal.objects.get(id=2)

		tmp["portal"] = portal
		del tmp['prt_uid']

		print(tmp)
		Webtoon.objects.create(**tmp)

	pass