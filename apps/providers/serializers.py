from rest_framework import serializers

from apps.providers.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('name', 'email', 'phone', 'language', 'currency')


class ServiceAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceArea
        fields = ('provider', 'name', 'price', 'polygon')


