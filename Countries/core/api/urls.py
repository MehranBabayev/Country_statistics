from django.urls import path
from .import views 

urlpatterns = [

    path('bumpchart/', views.BumpchartListAPIView.as_view(), name='bumpchart-list'),
    path('sector/', views.SectorListAPIView.as_view(), name='sector'),  
    path('subsector/', views.SubsectorListAPIView.as_view(), name='subsector'),
    # path('country/', views.CountryListView.as_view(), name='country-list'),
    
    path('country/', views.CountryFilterView.as_view(), name='country_filter'),
    path('chart/', views.NewCountryFilterView.as_view(), name='chart_filter'),

    path('rank_differences/', views.RankDifferenceView.as_view(), name='rank_differences'),
   

    path('indicator/', views.IndicatorFilterView.as_view(), name='indicator-filter'),
    path('indicator/<str:indicator_name>/', views.AdvancedIndicatorFilterView.as_view(), name='advanced-indicator-filter'),
    
]