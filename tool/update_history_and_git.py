import os,re
from neolib import neoutil
import neolib
import shutil

from neolib.tool.update_history_and_git import UpdateInitAndCommit

class CurUpdateInitAndCommit(UpdateInitAndCommit):
	def push_all(self):
		#self.init_file ="../neo_django_server"
		os.system("git push origin master")
		#os.system("git push github master")
if __name__ == '__main__':
	print(neolib)
	msg = """
update drf and oauth2
 
 


	"""
	CurUpdateInitAndCommit(init_file="../neo_django_server/__init__.py").run(msg)
	#commmit("1.2.3",msg)

	#main(msg)
	# version = change_init(msg)
	# commmit(version)
	# push_all()