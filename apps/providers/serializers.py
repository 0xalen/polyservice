import json
from decimal import Decimal
from unicodedata import decimal

import simplejson
from django.contrib.gis.forms import PolygonField
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
    """
    Serialization of ServiceArea Models.
    'provider' field is serialized as an IntegerField instead of using ProviderSerializer because of depth restrictions
    in the creation of nested objects.
    In this way, it's essentially a read-only field:
        provider = ProviderSerializer() -> provider = IntegerField()
    """
    provider = IntegerField()
    polygon = Polygon.json
    price = DecimalSerializer()

    class Meta:
        model = ServiceArea
        depth = 1
        fields = ('provider', 'name', 'price', 'polygon')


class ServiceAreaGeoSerializer(GeoFeatureModelSerializer):
    provider = IntegerField()
    price = DecimalSerializer()
    polygon = serialize(
        'geojson',
        ServiceArea.objects.all(),
        geometry_field='polygon',
        fields=('polygon',)
    )

    class Meta:
        model = ServiceArea
        depth = 2
        fields = ('provider', 'name', 'price', 'polygon')
        geo_field = "polygon"

