from rest_framework import generics
from api.serializers import PersonSerializer
from api.models import Person


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
