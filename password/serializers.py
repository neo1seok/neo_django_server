

from rest_framework import serializers

from .models import Password,PasswordHeader


class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ('pheader_id', 'site','ptail','site_id','etc','status')

class PasswordHeaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PasswordHeader
        fields = ('title', 'hint','special_letter','etc')