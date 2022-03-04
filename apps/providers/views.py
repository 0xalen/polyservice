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
    Class in charge of handling operations related particular instances of the Provider modal in the API.
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

        return Response({})

    def put(self, request, pk: int):
        """
        Update information about a particular provider.
        """
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            provider_data = request.PUT.get('data')
            serialized_provider = ProviderSerializer(provider_data)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        provider.updated_at()
        return Response({})

    def post(self, request):
        provider_data = request.data
        serialized_provider = ProviderSerializer(data=provider_data)
        if not serialized_provider.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized_provider.save()
        return Response(status=status.HTTP_201_CREATED)


class ProviderListView(APIView):
    """
    Class in charge of handling operations related to group of instances of the Provider modal in the API.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        provider_list = Provider.objects.all().order_by('name')
        if not provider_list.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        serialized_provider_list = ProviderSerializer(provider_list, many=True)
        provider_list_data = serialized_provider_list.data
        return Response(provider_list_data)

