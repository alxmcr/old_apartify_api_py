from api.models import Country, Person, State
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "co_country",
            "co_name",
            "co_abbr",
            "co_url",
            "co_alt",
        ]

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [
            "st_state",
            "st_name",
            "st_abbr",
            "st_url",
            "st_alt",
        ]