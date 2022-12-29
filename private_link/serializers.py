

from rest_framework import serializers

from .models import PrvLink


class PrvLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PrvLink
        fields = ('title', 'link','status')