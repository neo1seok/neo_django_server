import django_filters
from .models import Webtoon

class WebtoonFilter(django_filters.FilterSet):
    dates = django_filters.CharFilter(field_name='dates', lookup_expr='contains')
    class Meta:
        model = Webtoon
        fields = ['status','dates']
