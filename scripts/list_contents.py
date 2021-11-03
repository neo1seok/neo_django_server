
from datetime import datetime
import sys, os

from password.models import Password


Password
def run():
	print("start")
	for f in Password.objects.all():
		print(f)
