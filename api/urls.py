from django.urls import re_path
from django.urls import path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path("v2/countries", views.CountryList.as_view()),
    path("v2/countries/<int:pk>", views.CountryDetails.as_view()),
    path("v2/states", views.StateList.as_view()),
    path("v2/states/<int:pk>", views.StateDetails.as_view()),
    path("v2/cities", views.CityList.as_view()),
    path("v2/cities/<int:pk>", views.CityDetails.as_view()),
    path("v2/cities_hall", views.CityHallList.as_view()),
    path("v2/cities_hall/<int:pk>", views.CityHallDetails.as_view()),
    path("v2/neighborhoods", views.NeighborhoodList.as_view()),
    path("v2/neighborhoods/<int:pk>", views.NeighborhoodDetails.as_view()),
    path("v2/features", views.FeatureList.as_view()),
    path("v2/features/<int:pk>", views.FeatureDetails.as_view()),
    path("v2/outdoor_spaces", views.OutdoorSpaceList.as_view()),
    path("v2/outdoor_spaces/<int:pk>", views.OutdoorSpaceDetails.as_view()),
    path("v2/investments", views.InvestmentList.as_view()),
    path("v2/investments/<int:pk>", views.InvestmentDetails.as_view()),
    path("v2/apartments", views.ApartmentList.as_view()),
    path("v2/apartments/<int:pk>", views.ApartmentDetails.as_view()),
    path("v2/photos", views.PhotoList.as_view()),
    path("v2/photos/<int:pk>", views.PhotoDetails.as_view()),
    path("v2/floor_plans", views.FloorPlanList.as_view()),
    path("v2/floor_plans/<int:pk>", views.FloorPlanDetails.as_view()),
    # N:N + intermediate table
    path("v2/attracts", views.AttractList.as_view()),
    path("v2/outdoors", views.OutdoorList.as_view()),
    path("v2/invests", views.InvestList.as_view()),
]
