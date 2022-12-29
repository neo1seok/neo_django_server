

from rest_framework import serializers

from .models import Webtoon


class WebtoonSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="webtoon:user-detail")
    class Meta:
        model = Webtoon
        fields = ('portal_id', 'title','today_title','wid','lastno','dates','status')