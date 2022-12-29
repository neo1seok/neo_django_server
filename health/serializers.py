

from rest_framework import serializers

from .models import HealthBp,HealthWeight


class HealthBpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthBp
        fields = ('sys_bp', 'dia_bp','pulse','param','status')

class HealthWeightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthWeight
        fields = ('weight', 'param','status')
