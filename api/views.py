from django.http import HttpResponse
import json
from rest_framework.views import APIView
from api.serializers import ApartmentSerializer, AttractSerializer, CityHallSerializer, CitySerializer, CountrySerializer, FeatureSerializer, FloorPlanSerializer, InvestSerializer, InvestmentSerializer, NeighborhoodSerializer, OutdoorSerializer, OutdoorSpaceSerializer, PhotoSerializer, StateSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from api.models import Apartment, Attract, City, CityHall, Country, Feature, FloorPlan, Invest, Investment, Neighborhood, Outdoor, OutdoorSpace, Photo, State

def index(request):
    welcome_message = {'message': 'Welcome to Apartify API v2!'}
    return HttpResponse(json.dumps(welcome_message, indent=4, sort_keys=True), content_type="application/json")

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['co_name', 'co_abbr']

class CountryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['st_name', 'st_abbr']

class StateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ci_name', 'ci_abbr']

class CityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityHallList(generics.ListCreateAPIView):
    queryset = CityHall.objects.all()
    serializer_class = CityHallSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ch_name', 'ch_abbr']

class CityHallDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CityHall.objects.all()
    serializer_class = CityHallSerializer

class NeighborhoodList(generics.ListCreateAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ne_name', 'ne_abbr']

class NeighborhoodDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Neighborhood.objects.all()
    serializer_class = NeighborhoodSerializer

class FeatureList(generics.ListCreateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['fe_type', 'fe_name']

class FeatureDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class OutdoorSpaceList(generics.ListCreateAPIView):
    queryset = OutdoorSpace.objects.all()
    serializer_class = OutdoorSpaceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ou_type', 'ou_name']

class OutdoorSpaceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = OutdoorSpace.objects.all()
    serializer_class = OutdoorSpaceSerializer

class InvestmentList(generics.ListCreateAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['in_type', 'in_name']

class InvestmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class ApartmentList(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ap_cost_offer', 'ap_cost_list', 'ap_floor_number']

class ApartmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ap_apartment', 'ph_url']

class PhotoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class FloorPlanList(generics.ListCreateAPIView):
    queryset = FloorPlan.objects.all()
    serializer_class = FloorPlanSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ap_apartment', 'fp_url']

class FloorPlanDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = FloorPlan.objects.all()
    serializer_class = FloorPlanSerializer

# N:N + intermediate table
class AttractList(generics.ListCreateAPIView):
    queryset = Attract.objects.all()
    serializer_class = AttractSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ap_apartment', 'fe_feature']

class AttractDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attract.objects.all()
    serializer_class = AttractSerializer

class OutdoorList(generics.ListCreateAPIView):
    queryset = Outdoor.objects.all()
    serializer_class = OutdoorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ap_apartment', 'ou_outdoor_space']

class OutdoorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outdoor.objects.all()
    serializer_class = OutdoorSerializer    

class InvestList(generics.ListCreateAPIView):
    queryset = Invest.objects.all()
    serializer_class = InvestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ap_apartment', 'in_investment']

class InvestDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invest.objects.all()
    serializer_class = InvestSerializer