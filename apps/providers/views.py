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

        return Response({})

    def delete(self, pk: int):
        """
        Delete a provider.
        """
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response({})

    def put(self, pk: int):
        """
        Update information about a particular provider.
        """
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response({})

    def post(self, pk: int):
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response({})


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

        return Response({})

