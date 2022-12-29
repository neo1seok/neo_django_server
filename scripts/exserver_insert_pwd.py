
#import pymysql

import pymysql
from neolib import neoutil

from password.models import PasswordHeader, Password



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
			SELECT seq, phd_uid, title, hint, special_letter, etc, updt_date, reg_date, comment 
			FROM neo_pwinfo.pheader;""")
	list_map_portal = cur.fetchall()
	map_data ={}
	PasswordHeader.objects.all().delete()
	for tmp in list_map_portal:
		tmp['id'] = tmp['seq']
		del tmp['seq']
		phd_uid = tmp['phd_uid']
		del tmp['phd_uid']
		del tmp['comment']

		pheader = PasswordHeader.objects.create(**tmp)
		map_data[phd_uid] = pheader

	#exit()
	cur.execute("""
		SELECT seq, phd_uid, site, ptail, id, etc, status, updt_date, reg_date  
FROM neo_pwinfo.passwd;
""")
	list_map = cur.fetchall()
	Password.objects.all().delete()
	for tmp in list_map:
		tmp['id'] =  tmp['seq']
		del tmp['seq']

		print(tmp)
		phd_uid =  tmp.get('phd_uid')
		if not phd_uid: continue

		tmp["pheader"] = map_data[phd_uid]
		del tmp['phd_uid']



		Password.objects.create(**tmp)

	pass