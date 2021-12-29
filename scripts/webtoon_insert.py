
#import pymysql

import pymysql
from neolib import neoutil

from webtoon.models import Webtoon


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
		FROM neo_pwinfo.webtoon;""")
	list_map = cur.fetchall()
	for tmp in list_map:
		del tmp['seq']
		del tmp['wtn_uid']
		tmp['wid'] = tmp['id']
		del tmp['id']
		del tmp['prt_uid']



		Webtoon.objects.create(**tmp)
		print(list_map)
	pass