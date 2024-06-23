

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Password,PasswordHeader



class PasswordHeaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PasswordHeader
        fields = ('title', 'hint','special_letter','etc')

class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    pheader_id = PrimaryKeyRelatedField(read_only=True,source="pheader")#ForeignKey 의 id로 표시 한다.
    pheader = PasswordHeaderSerializer(read_only=True)# ForeignKey 를 json 형태로 표기 한다.
    class Meta:
        model = Password
        fields = ('pheader_id', 'pheader','site','ptail','site_id','etc','status')
