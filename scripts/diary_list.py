import json
import os

from attributedict.collections import AttributeDict

from diary.models import DiaryContents

from neolib import neoutil


def run():
	for f in DiaryContents.objects.all():
		print(f, f.status)
# break


