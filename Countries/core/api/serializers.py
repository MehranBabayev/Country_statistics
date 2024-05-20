from rest_framework import serializers
from core.models import Sector, Subsector, Indicator, Countries



class CountryChartRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['year',  'country',  'amount', 'rank']


class CountryBumpchartRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['year',  'country',  'amount']



class IndicatorChartSerializer(serializers.ModelSerializer):
    countryrating = CountryChartRatingSerializer(many=True)
    
    class Meta:
        model = Indicator
        fields = [ 'indicator','countryrating' ]


class IndicatorBumpchartSerializer(serializers.ModelSerializer):
    countryrating = CountryBumpchartRatingSerializer(many=True)
    
    class Meta:
        model = Indicator
        fields = [ 'indicator','countryrating' ]



class IndicatorSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Indicator
        fields = [ 'indicator']


class SubsectorSerializer(serializers.ModelSerializer):
    indicator = IndicatorSerializer
    class Meta:
        model = Subsector
        fields = [ 'subsector','indicator']



class SectorSerializer(serializers.ModelSerializer):
    subsector = SubsectorSerializer(many=True)
    class Meta:
        model = Sector
        fields = ['sector', 'subsector']
        
        
        






class CountryFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = ['country']






from rest_framework import serializers

class RankDifferenceSerializer(serializers.Serializer):
    indicator_name = serializers.CharField()
    rank_difference = serializers.IntegerField()
    country = serializers.CharField() 



