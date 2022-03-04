from django.contrib.gis.geos import Polygon, Point
from django.db.models import Func
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status, permissions
from apps.providers.models import Provider, ServiceArea
from apps.providers.serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderInformationView(APIView):
    """
    Class in charge of handling operations related particular instances of the Provider model in the API.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk: int):
        """
        Get details from a particular provider.
        """
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized_provider = ProviderSerializer(provider)
        provider_detail_data = serialized_provider.data
        return Response(provider_detail_data)

    def delete(self, request, pk: int):
        """
        Delete a provider.
        """
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk: int):
        """
        Update information about a particular provider.
        """
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        provider_data = request.data
        serialized_provider = ProviderSerializer(provider, data=provider_data)
        if not serialized_provider.is_valid():
            return Response(serialized_provider.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serialized_provider.data, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        provider_data = request.data
        serialized_provider = ProviderSerializer(data=provider_data)
        if not serialized_provider.is_valid():
            return Response(serialized_provider.errors, status=status.HTTP_400_BAD_REQUEST)

        serialized_provider.save()
        return Response(serialized_provider.data, status=status.HTTP_201_CREATED)


class ProviderListView(APIView):
    """
    Class in charge of handling operations related to group of instances of the Provider model in the API.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        provider_list = Provider.objects.all().order_by('name')
        serialized_provider_list = ProviderSerializer(provider_list, many=True)

        return Response(serialized_provider_list.data, status=status.HTTP_200_OK)


class ServiceAreaInformationView(APIView):
    """
        Class in charge of handling operations related particular instances of the ServiceArea model in the API.
        """
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk: int):
        """
        Get details from a particular service area.
        """
        try:
            service_area = ServiceArea.objects.get(pk=pk)
        except ServiceArea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized_service_area = ServiceAreaSerializer(service_area)
        service_area_detail_data = serialized_service_area.data
        return Response(service_area_detail_data)

    def delete(self, request, pk: int):
        """
        Delete a service area.
        """
        try:
            service_area = ServiceArea.objects.get(pk=pk)
        except ServiceArea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        service_area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk: int):
        """
        Update information about a particular service area.
        """
        try:
            service_area = ServiceArea.objects.get(pk=pk)
        except ServiceArea.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        service_area_data = request.data
        serialized_service_area = ServiceAreaSerializer(service_area, data=service_area_data)
        if not serialized_service_area.is_valid():
            return Response(serialized_service_area.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serialized_service_area.data, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        service_area_data = request.data

        serialized_service_area = ServiceAreaSerializer(data=service_area_data)
        if not serialized_service_area.is_valid():
            return Response(serialized_service_area.errors, status=status.HTTP_400_BAD_REQUEST)

        serialized_service_area.save()
        return Response(serialized_service_area.data, status=status.HTTP_201_CREATED)


class ServiceAreaListView(APIView):
    """
    Class in charge of handling operations related to group of instances of the ServiceArea model in the API.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service_area_list = ServiceArea.objects.all().order_by('name')
        serialized_service_area_list = ServiceAreaSerializer(service_area_list, many=True)

        return Response(serialized_service_area_list.data, status=status.HTTP_200_OK)


class FindServiceAreasView(APIView):
    """
    Class in charge of handling queries of involving ServiceAreas in the API.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        location_data = request.data
        location = Point(
            location_data.get('lon'),
            location_data.get('lat'),
        )

        # TODO -> Review query
        service_area_list_by_location = ServiceArea.objects.filter(
            polygon__contains=location
        ).order_by('provider')

        serialized_service_area_list = ServiceAreaSerializer(service_area_list_by_location, many=True)
        return Response(serialized_service_area_list.data, status=status.HTTP_200_OK)

