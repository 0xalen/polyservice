import json
from decimal import Decimal
from unicodedata import decimal

from django.contrib.gis.geos import Polygon
from django.core.serializers import serialize
from django.core.signing import JSONSerializer
from django.db.models import IntegerField

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from apps.providers.encoders import DecimalEncoder
from apps.providers.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('name', 'email', 'phone', 'language', 'currency')


class DecimalSerializer(JSONSerializer):
    def end_serialization(self):
        self.options.pop('stream', None)
        self.options.pop('fields', None)
        json.dump(self.objects, self.stream, cls=DecimalEncoder, **self.options)


class ServiceAreaSerializer(serializers.ModelSerializer):
    # provider = ProviderSerializer()
    provider = IntegerField()
    polygon = Polygon.json
    price = DecimalSerializer()

    class Meta:
        model = ServiceArea
        depth = 1
        fields = ('provider', 'name', 'price', 'polygon')


