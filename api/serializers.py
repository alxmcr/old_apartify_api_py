from api.models import Apartment, City, Country, Feature, Flat, Investment, Neighborhood, OutdoorSpace, Photo, State
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

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "ci_city",
            "ci_name",
            "ci_abbr",
            "ci_url",
            "ci_alt",
        ]

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = [
            "ne_neighborhood",
            "ne_name",
            "ne_abbr",
            "ne_url",
            "ne_alt",
        ]

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields =  [
            "fe_feature",
            "fe_type",
            "fe_name",
            "fe_icon_url",
            "fe_icon_color",
            "fe_is_visible",
            "fe_is_card",
        ]

class OutdoorSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutdoorSpace
        fields = [
            "ou_outdoor_space",
            "ou_type",
            "ou_name",
            "ou_icon_url",
            "ou_icon_color",
            "ou_is_visible",
            "ou_is_card",
        ]

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = [
            "in_investment",
            "in_type",
            "in_name",
            "in_icon_url",
            "in_icon_color",
            "in_is_visible",
            "in_is_card",
        ]

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = [
            "ap_apartment",
            "ap_descripcion",
            "ap_floor_number",
            "ap_cost_offer",
            "ap_cost_list",
            "ap_is_remodeling",
            "ap_latitude",
            "ap_longitude",
            "ap_street_name",
            "ap_ext_number",
            "ap_int_number",
            "ne_neighborhood",
            "ci_city",
            "co_country",
            "st_state",
            "features",
            "outdoor_spaces",
            "investments",
        ]

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "ph_photo",
            "ph_url",
            "ph_alt",
            "ap_apartment",
        ]

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = [
            "fl_flat",
            "fl_url",
            "fl_alt",
            "ap_apartment",
        ]
