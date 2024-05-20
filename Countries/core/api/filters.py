import django_filters
from core.models import Countries, Indicator

class CountryFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country', lookup_expr='iexact')
    id = django_filters.NumberFilter(field_name='id')  # Add this line
    year = django_filters.NumberFilter(field_name='year')  # Add this line
    indicator = django_filters.CharFilter(field_name='indicator__indicator', lookup_expr='iexact')  # Add this line

    class Meta:
        model = Countries
        fields = ['country', 'id', 'year', 'indicator']





import django_filters
from core.models import Countries

class IndicatorFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country', lookup_expr='iexact')
    year = django_filters.NumberFilter(field_name='year')
    id = django_filters.NumberFilter(field_name='id')
    class Meta:
        model = Countries
        fields = ['country', 'year','id',]
