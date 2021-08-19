from api.serializers import ApartmentSerializer, AttractSerializer, CityHallSerializer, CitySerializer, CountrySerializer, FeatureSerializer, FloorPlanSerializer, InvestSerializer, InvestmentSerializer, NeighborhoodSerializer, OutdoorSerializer, OutdoorSpaceSerializer, PhotoSerializer, StateSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Apartment, Attract, City, CityHall, Country, Feature, FloorPlan, Invest, Investment, Neighborhood, Outdoor, OutdoorSpace, Photo, State


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['co_name']

class CountryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityHallList(generics.ListCreateAPIView):
    queryset = CityHall.objects.all()
    serializer_class = CityHallSerializer

class CityHallDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CityHall.objects.all()
    serializer_class = CityHallSerializer

class NeighborhoodList(generics.ListCreateAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class NeighborhoodDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class FeatureList(generics.ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class FeatureDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class OutdoorSpaceList(generics.ListCreateAPIView):
    queryset = OutdoorSpace.objects.all()
    serializer_class = OutdoorSpaceSerializer

class OutdoorSpaceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = OutdoorSpace.objects.all()
    serializer_class = OutdoorSpaceSerializer

class InvestmentList(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class ApartmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class FloorPlanList(generics.ListCreateAPIView):
    queryset = FloorPlan.objects.all()
    serializer_class = FloorPlanSerializer

class FloorPlanDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = FloorPlan.objects.all()
    serializer_class = FloorPlanSerializer

# N:N + intermediate table
class AttractList(generics.ListCreateAPIView):
    queryset = Attract.objects.all()
    serializer_class = AttractSerializer

class AttractDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attract.objects.all()
    serializer_class = AttractSerializer

class OutdoorList(generics.ListCreateAPIView):
    queryset = Outdoor.objects.all()
    serializer_class = OutdoorSerializer

class OutdoorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outdoor.objects.all()
    serializer_class = OutdoorSerializer    

class InvestList(generics.ListCreateAPIView):
    queryset = Invest.objects.all()
    serializer_class = InvestSerializer

class InvestDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invest.objects.all()
    serializer_class = InvestSerializer