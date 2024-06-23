from django.forms import model_to_dict
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Webtoon,Portal
class PortalSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="webtoon:user-detail")
    class Meta:
        model = Portal
        #fields = ('portal', 'title','today_title','wid','lastno','dates','status')
        fields = ( 'name', 'search_form', 'list_webtoon','list_webtoon_m', 'contents_webtoon','contents_webtoon_m', 'main_url', 'etc','img_url')

class WebtoonSerializer(serializers.HyperlinkedModelSerializer):
    portal_id = PrimaryKeyRelatedField(read_only=True,source="portal")#ForeignKey 의 id로 표시 한다.
    portal = PortalSerializer(read_only=True)# ForeignKey 를 json 형태로 표기 한다.
    contents_webtoon = serializers.SerializerMethodField()
    list_webtoon = serializers.SerializerMethodField()
    contents_webtoon_m = serializers.SerializerMethodField()
    list_webtoon_m = serializers.SerializerMethodField()
    main_img_url = serializers.SerializerMethodField()
    class Meta:
        model = Webtoon
        #fields = ('portal', 'title','today_title','wid','lastno','dates','status')
        fields = ('portal','portal_id','title', 'today_title', 'title_id', 'lastno', 'dates', 'status','updt_date','reg_date','contents_webtoon','list_webtoon','contents_webtoon_m','list_webtoon_m','main_img_url')

    def get_contents_webtoon(self, obj):
        # portal의 contents_webtoon 필드에 lastno와 wid 값을 포맷하여 삽입
        return obj.portal.contents_webtoon.format(**model_to_dict (obj))

    def get_list_webtoon(self, obj):
        # portal의 contents_webtoon 필드에 lastno와 wid 값을 포맷하여 삽입
        return obj.portal.list_webtoon.format(**model_to_dict(obj))

    def get_contents_webtoon_m(self, obj):
        # portal의 contents_webtoon 필드에 lastno와 wid 값을 포맷하여 삽입
        return obj.portal.contents_webtoon_m.format(**model_to_dict(obj))

    def get_list_webtoon_m(self, obj):
        # portal의 contents_webtoon 필드에 lastno와 wid 값을 포맷하여 삽입
        return obj.portal.list_webtoon_m.format(**model_to_dict(obj))
    def get_main_img_url(self, obj):
        # portal의 contents_webtoon 필드에 lastno와 wid 값을 포맷하여 삽입
        return obj.portal.img_url.format(**model_to_dict(obj))
