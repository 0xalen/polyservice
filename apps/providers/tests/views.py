import json
# from rest_framework.authtoken.admin import User
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from apps.providers.models import Provider, ServiceArea
from apps.providers.serializers import ProviderSerializer, ServiceAreaSerializer
from apps.providers.tests.data import *
from apps.providers.tests.models import TestModelsBase


class TestProvidersBase(TestProvidersUrlsBase):

    @classmethod
    def setUpTestData(cls):
        cls.__setUpUsers()

    @classmethod
    def __setUpUsers(cls):
        """
        Test users are created using the SessionAuthentication class for simplicity.
        Since the authentication_classes also include TokenAuthentication and BasicAuthentication, either of them
        could've been used as well.
        """
        User.objects.create_user(username=API_USER, password=API_USER_PASSWORD)


class TestProviderInformationView(TestProvidersBase):
    """
    Class for testing ProviderInformationView.
    Run:
        python manage.py test apps.providers.tests.views.TestProviderInformationView --keepdb
    """

    def setUp(self):
        self.provider_1 = Provider.objects.create(
            name=PROVIDER_1,
            email=EMAIL_1,
            phone=PHONE_NUMBER_1,
            language=LANGUAGE_1,
            currency=CURRENCY_1,
        )
        self.TEST_ID_1 = self.provider_1.id
        self.provider_2 = Provider.objects.create(
            name=PROVIDER_2,
            email=EMAIL_2,
            phone=PHONE_NUMBER_2,
            language=LANGUAGE_2,
            currency=CURRENCY_1,
        )
        self.TEST_ID_2 = self.provider_2.id
        self.valid_provider_data = {
            'name': "Valid provider",
            'email': "valid@email.fake",
            'phone': PHONE_NUMBER_1,
            'language': LANGUAGE_1,
            'currency': CURRENCY_1
        }
        self.invalid_provider_data = {
            'name': None,
            'email': "invalidemail.fake",
            'phone': "1432432123A",
            'language': 'en',
            'currency': '$'
        }

    def test_get_detail_unauthenticated_GET_response_forbidden(self):
        response = self.client.get(self.url_get_provider_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_detail_authenticated_GET_response_ok(self):
        self.client.login(username=API_USER, password=API_USER_PASSWORD)
        url_get_provider_detail = reverse('providers:provider_detail', kwargs={'pk': self.TEST_ID_1})
        response = self.client.get(url_get_provider_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_provider_delete_unauthenticated_DELETE_response_forbidden(self):
        response = self.client.delete(self.url_delete_provider)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_provider_delete_authenticated_DELETE_response_ok(self):
        self.client.login(username=API_USER, password=API_USER_PASSWORD)

        url_delete_provider = reverse('providers:provider_delete', kwargs={'pk': self.TEST_ID_1})
        response = self.client.delete(url_delete_provider)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_provider_update_unauthenticated_PUT_response_forbidden(self):
        response = self.client.put(self.url_update_provider_information)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_provider_update_authenticated_PUT_response_ok(self):
        self.client.login(username=API_USER, password=API_USER_PASSWORD)
        url_update_provider_information = reverse('providers:provider_update', kwargs={'pk': self.TEST_ID_1})
        response = self.client.get(url_update_provider_information)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_provider_creation_unauthenticated_POST_response_forbidden(self):
        response = self.client.post(self.url_create_provider)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_provider_creation_authenticated_POST_invalid_data_response_bad(self):
        self.client.login(username=API_USER, password=API_USER_PASSWORD)
        url_create_provider = reverse('providers:provider_creation')
        provider_data = json.dumps(self.invalid_provider_data)
        response = self.client.post(
            url_create_provider,
            data=provider_data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_provider_creation_authenticated_POST_valid_data_response_created(self):
        self.client.login(username=API_USER, password=API_USER_PASSWORD)
        url_create_provider = reverse('providers:provider_creation')
        provider_data = json.dumps(self.valid_provider_data)

        response = self.client.post(
            url_create_provider,
            data=provider_data,
            content_type='application/json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestProviderListView(TestProvidersBase):
    """
    Class for testing ProviderListView.
    Run:
        python manage.py test apps.providers.tests.views.TestProviderListView
    """

    def setUp(self):
        for i in range(10):
            Provider.objects.create(
                name=f"PROVIDER {i}",
                email=EMAIL_1,
                phone=PHONE_NUMBER_1,
                language=LANGUAGE_1,
                currency=CURRENCY_1,
            )

    def test_get_all_providers_unauthenticated_GET_response_forbidden(self):
        response = self.client.get(self.url_get_provider_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_providers_authenticated_receives_data(self):
        self.client.login(username=API_USER, password=API_USER_PASSWORD)
        provider_list = Provider.objects.all()
        provider_serializer = ProviderSerializer(provider_list, many=True)
        response = self.client.get(self.url_get_provider_list)

        self.assertEqual(response.data, provider_serializer.data)


