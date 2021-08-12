from rest_framework import generics
from api.serializers import CountrySerializer, PersonSerializer
from api.models import Country, Person


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer