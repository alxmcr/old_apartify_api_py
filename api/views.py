from api.serializers import ApartmentSerializer, CitySerializer, CountrySerializer, FeatureSerializer, FlatSerializer, InvestmentSerializer, NeighborhoodSerializer, OutdoorSpaceSerializer, PhotoSerializer, StateSerializer
from rest_framework import generics
from api.models import Apartment, City, Country, Feature, Flat, Investment, Neighborhood, OutdoorSpace, Photo, State


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class NeighborhoodList(generics.ListCreateAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class FeatureList(generics.ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class OutdoorSpaceList(generics.ListCreateAPIView):
    queryset = OutdoorSpace.objects.all()
    serializer_class = OutdoorSpaceSerializer

class InvestmentList(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class FlatList(generics.ListCreateAPIView):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer