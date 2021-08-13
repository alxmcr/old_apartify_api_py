from api.serializers import ApartmentSerializer, AttractSerializer, CityHallSerializer, CitySerializer, CountrySerializer, FeatureSerializer, FlatSerializer, InvestSerializer, InvestmentSerializer, NeighborhoodSerializer, OutdoorSerializer, OutdoorSpaceSerializer, PhotoSerializer, StateSerializer
from rest_framework import generics
from api.models import Apartment, Attract, City, CityHall, Country, Feature, Flat, Invest, Investment, Neighborhood, Outdoor, OutdoorSpace, Photo, State


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityHallList(generics.ListCreateAPIView):
    queryset = CityHall.objects.all()
    serializer_class = CityHallSerializer

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

# N:N + intermediate table
class AttractList(generics.ListCreateAPIView):
    queryset = Attract.objects.all()
    serializer_class = AttractSerializer

class OutdoorList(generics.ListCreateAPIView):
    queryset = Outdoor.objects.all()
    serializer_class = OutdoorSerializer

class InvestList(generics.ListCreateAPIView):
    queryset = Invest.objects.all()
    serializer_class = InvestSerializer