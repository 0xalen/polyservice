from django.conf.global_settings import LANGUAGES
from django.conf import settings
from django.test import TestCase
from djmoney.models.fields import MoneyField
from .data import *

from apps.providers.models import Provider, ServiceArea


class TestModelsBase(TestCase):
    """
    Class for testing models in the providers app.
    Run:
        python manage.py test apps.providers.tests.models.TestModelsBase --keepdb
    """

    @classmethod
    def setUpTestData(cls):
        cls.__setUpProviders()
        cls.__setUpServiceAreas()

    @classmethod
    def __setUpProviders(cls):
        cls.provider_1 = Provider.objects.create(
            name=PROVIDER_1,
            email=EMAIL_1,
            phone=PHONE_NUMBER_1,
            language=LANGUAGE_1,
            currency=CURRENCY_1,
        )
        cls.provider_2 = Provider.objects.create(
            name=PROVIDER_2,
            email=EMAIL_2,
            phone=PHONE_NUMBER_2,
            language=LANGUAGE_2,
            currency=CURRENCY_1,
        )

    @classmethod
    def __setUpServiceAreas(cls):
        cls.service_area_1 = ServiceArea.objects.create(
            provider=Provider.objects.get(name=PROVIDER_1),
            name=SERVICE_AREA_1,
            price=PRICE_1,
            polygon=POLYGON_1,
        )
        cls.service_area_2 = ServiceArea.objects.create(
            provider=Provider.objects.get(name=PROVIDER_1),
            name=SERVICE_AREA_2,
            price=PRICE_2,
            polygon=POLYGON_2,
        )

    def test_provider_created_correctly(self):
        provider_1 = Provider.objects.get(name=PROVIDER_1)

        self.assertEqual(provider_1, self.provider_1)

    def test_service_area_created_correctly(self):
        service_area_1 = ServiceArea.objects.get(name=SERVICE_AREA_1)

        self.assertEqual(service_area_1, self.service_area_1)


class TestProvider(TestModelsBase):
    """
    Class for testing Provider model.
    Run:
        python manage.py test apps.providers.tests.models.TestProvider --keepdb
    """

    def test_string_representation(self):
        provider_1 = self.provider_1
        expected_string = PROVIDER_1
        received_string = str(provider_1)

        self.assertEqual(expected_string, received_string)


class TestServiceArea(TestModelsBase):
    """
    Class for testing ServiceArea model.
    Run:
        python manage.py test apps.providers.tests.models.TestServiceArea --keepdb
    """

    def test_string_representation(self):
        service_area_1 = self.service_area_1

        expected_string = SERVICE_AREA_1
        received_string = str(service_area_1)
        self.assertEqual(expected_string, received_string)

    def test_get_formatted_price(self):
        expected_value = PRICE_1
        service_area_1 = self.service_area_1
        received_value = service_area_1.get_formatted_price()

        self.assertEqual(expected_value, received_value)

    def test_many_service_areas_to_one_provider(self):
        provider_2 = self.provider_2
        service_areas_count_expected = 3

        service_area_list = [
            ServiceArea.objects.create(
                provider=provider_2,
                name=SERVICE_AREA_2,
                price=PRICE_2,
                polygon=POLYGON_2
            ) for _ in range(service_areas_count_expected)
        ]

        service_area_count_received = len(service_area_list)
        self.assertEqual(service_areas_count_expected, service_area_count_received)

