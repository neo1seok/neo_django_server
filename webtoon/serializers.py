

from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Webtoon,Portal
class PortalSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="webtoon:user-detail")
    class Meta:
        model = Portal
        #fields = ('portal', 'title','today_title','wid','lastno','dates','status')
        fields = ( 'name', 'search_form', 'list_webtoon', 'contents_webtoon', 'main_url', 'etc')

class WebtoonSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="webtoon:user-detail")
    #portal = PortalSerializer(many=True, read_only=True)
    #portal_id = serializers.IntegerField(source='portal.id')
    #portal_name = serializers.CharField(source='portal.name')
    #portal_obj = serializers.JSONField(source='portal')
    #portal_obj = serializers.JSONField(source='portal')
    portal_id = PrimaryKeyRelatedField(read_only=True,source="portal")#ForeignKey 의 id로 표시 한다.
    portal = PortalSerializer(read_only=True)# ForeignKey 를 json 형태로 표기 한다.
    class Meta:
        model = Webtoon
        #fields = ('portal', 'title','today_title','wid','lastno','dates','status')
        fields = ('portal','portal_id','title', 'today_title', 'wid', 'lastno', 'dates', 'status')