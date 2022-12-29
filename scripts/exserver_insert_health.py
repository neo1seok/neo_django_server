
#import pymysql

import pymysql
from neolib import neoutil

from health.models import HealthBp,HealthWeight




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
			SELECT sys_bp, dia_bp, pulse, param,  status, updt_date, reg_date, comment 
FROM neo_pwinfo.health where type = 'BP';
""")
	list_map_bp = cur.fetchall()

	cur.execute("""
				SELECT weight, param,  status, updt_date, reg_date, comment 
	FROM neo_pwinfo.health where type = 'WT';
	""")
	list_map_weight = cur.fetchall()

	map_data ={}
	HealthBp.objects.all().delete()
	HealthWeight.objects.all().delete()
	idx_bp = 1
	idx_wt = 1

	for tmp in list_map_bp:
		tmp['id'] = idx_bp
		tmp['param']= tmp['comment']
		del tmp['comment']
		HealthBp.objects.create(**tmp)
		idx_bp +=1

	for tmp in list_map_weight:
		tmp['id'] = idx_wt
		tmp['param'] = tmp['comment']
		del tmp['comment']
		HealthWeight.objects.create(**tmp)
		idx_wt +=1

