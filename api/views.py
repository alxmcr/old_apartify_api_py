from api.serializers import CountrySerializer
from rest_framework import generics
from api.models import Country


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer