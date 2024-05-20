from rest_framework.generics import ListAPIView
from core.models import Sector, Subsector, Indicator, Countries
from .serializers import (
    SectorSerializer,
    SubsectorSerializer, 
    IndicatorSerializer,
    IndicatorChartSerializer,
    IndicatorBumpchartSerializer,
    CountryFilterSerializer,
    CountryChartRatingSerializer
)


from .filters import CountryFilter





class SectorListAPIView(ListAPIView):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer
    
    
    

class SubsectorListAPIView(ListAPIView):
    queryset = Subsector.objects.all()
    serializer_class = SubsectorSerializer
    
    
    

class ChartListAPIView(ListAPIView):
    queryset = Indicator.objects.all()[:1]
    serializer_class = IndicatorChartSerializer
    
    
    
    
class BumpchartListAPIView(ListAPIView):
    queryset = Indicator.objects.all()[:1]
    serializer_class = IndicatorBumpchartSerializer    



from rest_framework.generics import ListAPIView
from core.models import Indicator
from .serializers import IndicatorChartSerializer
from .filters import IndicatorFilter

class IndicatorFilterView(ListAPIView):
    serializer_class = IndicatorSerializer
    filterset_class = IndicatorFilter
    queryset = Indicator.objects.all()






# from rest_framework.generics import ListAPIView
# from core.models import Indicator
# from .serializers import IndicatorChartSerializer
# from .filters import IndicatorFilter

# class AdvancedIndicatorFilterView(ListAPIView):
#     serializer_class = IndicatorChartSerializer
#     filterset_class = IndicatorFilter  # Add this line

#     def get_queryset(self):
#         indicator_name = self.kwargs['indicator_name']

#         year = self.request.query_params.get('year')

#         queryset = Indicator.objects.filter(indicator=indicator_name)

#         if year:

#             queryset = queryset.filter(countryrating__year=year)

#         return queryset


from rest_framework.response import Response
from rest_framework.views import APIView

class AdvancedIndicatorFilterView(APIView):

    def get(self, request, indicator_name):
        year = request.query_params.get('year')
        country = request.query_params.get('counrty')
        

        queryset = Indicator.objects.filter(indicator=indicator_name, countryrating__country=country)

        if year:
            queryset = queryset.filter(countryrating__year=year)

        data = [
            {
                "indicator": item.indicator,
                "countryrating": [
                    {
                        "country": rating.country,
                        "year": rating.year,
                        "amount": rating.amount,
                        "rank": rating.rank,
                    } for rating in item.countryrating.all()
                ]
            } for item in queryset
        ]

        return Response(data)









    


from rest_framework import generics
from core.models import Countries
from .serializers import CountryChartRatingSerializer

class CountryFilterView(generics.ListAPIView):
    serializer_class = CountryChartRatingSerializer

    def get_queryset(self):
        indicator_name = self.request.query_params.get('indicator_name')
        year = self.request.query_params.get('year')
        country = self.request.query_params.get('country')

        queryset = Countries.objects.all()

        # Apply filters based on query parameters
        if indicator_name:
            queryset = queryset.filter(indicator__indicator=indicator_name)

        if year:
            queryset = queryset.filter(year=year)

        if country:
            queryset = queryset.filter(country__iexact=country)

        # Sort queryset by 'rank'
        queryset = queryset.order_by('rank')

        return queryset




from rest_framework import generics
from core.models import Countries
from .serializers import CountryBumpchartRatingSerializer

class NewCountryFilterView(generics.ListAPIView):
    serializer_class = CountryBumpchartRatingSerializer

    def get_queryset(self):
        indicator_name = self.request.query_params.get('indicator_name')
        year = self.request.query_params.get('year')
        country = self.request.query_params.get('country')

        queryset = Countries.objects.all()

        # Apply filters based on query parameters
        if indicator_name:
            queryset = queryset.filter(indicator__indicator=indicator_name)

        if year:
            queryset = queryset.filter(year=year)

        if country:
            queryset = queryset.filter(country__iexact=country)

        # Sort queryset by 'rank'
        queryset = queryset.order_by('-amount')

        return queryset





from rest_framework.generics import ListAPIView

class CountryListView(ListAPIView):
    serializer_class = CountryFilterSerializer
    queryset = Countries.objects.all()[:100]
        


from rest_framework import generics, serializers
from core.models import Indicator, Countries
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class RankDifferenceSerializer(serializers.Serializer):
    indicator_name = serializers.CharField()
    rank_difference = serializers.IntegerField()
    country = serializers.CharField()

class RankDifferenceView(generics.ListAPIView):
    serializer_class = RankDifferenceSerializer

    def get_queryset(self):
        indicator_name = self.request.query_params.get('indicator_name')
        year1 = self.request.query_params.get('year1')
        year2 = self.request.query_params.get('year2')

        try:
            indicator = Indicator.objects.get(indicator=indicator_name)
        except ObjectDoesNotExist:
            return Response({"error": "Indicator not found"}, status=status.HTTP_404_NOT_FOUND)

        countries_year1 = Countries.objects.filter(year=year1, indicator=indicator)
        countries_year2 = Countries.objects.filter(year=year2, indicator=indicator)

        rank_differences = []

        for country_year1 in countries_year1:
            country_year2 = countries_year2.filter(country=country_year1.country).first()

            if country_year2:
                rank_difference = country_year2.rank - country_year1.rank
                rank_differences.append({
                    "indicator_name": indicator_name,
                    "rank_difference": rank_difference,
                    "country": country_year1.country
                })

        # Order by max rank difference
        rank_differences = sorted(rank_differences, key=lambda x: x['rank_difference'], reverse=True)

        return rank_differences

       

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

