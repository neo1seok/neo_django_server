

from rest_framework import serializers

from .models import Webtoon


class WebtoonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Webtoon
        fields = ('portal', 'title','today_title','wid','lastno','dates','status')