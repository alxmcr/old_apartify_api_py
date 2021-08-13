from django.urls import path
from . import views

urlpatterns = [
    path("countries", views.CountryList.as_view()),
    path("states", views.StateList.as_view()),
    path("cities", views.CityList.as_view()),
    path("cities_hall", views.CityHallList.as_view()),
    path("neighborhoods", views.NeighborhoodList.as_view()),
    path("features", views.FeatureList.as_view()),
    path("outdoor_spaces", views.OutdoorSpaceList.as_view()),
    path("investments", views.InvestmentList.as_view()),
    path("apartments", views.ApartmentList.as_view()),
    path("photos", views.PhotoList.as_view()),
    path("flats", views.FlatList.as_view()),
    # N:N + intermediate table
    path("attracts", views.AttractList.as_view()),
    path("outdoors", views.OutdoorList.as_view()),
    path("invests", views.InvestList.as_view()),
]
