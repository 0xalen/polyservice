from django.conf.global_settings import LANGUAGES
from django.conf import settings
from django.test import TestCase
from djmoney.models.fields import MoneyField
from .data import *

from apps.providers.models import Provider, ServiceArea


class TestProvider(TestCase):
    """
    Class to test Provider model.
    python manage.py test apps.providers.tests.models.TestProvider --keepdb
    """

    def setUp(self):
        Provider.objects.create(
            name=PROVIDER_1,
            email=EMAIL_1,
            phone=PHONE_NUMBER_1,
            language=LANGUAGE_1,
            currency=CURRENCY_1,
        )
        Provider.objects.create(
            name=PROVIDER_2,
            email=EMAIL_2,
            phone=PHONE_NUMBER_2,
            language=settings.LANGUAGE_CODE,
            currency=CURRENCY_1,
        )

    def test_string_representation(self):
        provider_1 = Provider.objects.get(name=PROVIDER_1)

        expected_string = PROVIDER_1
        received_string = str(provider_1)
        self.assertEqual(expected_string, received_string)


class TestServiceArea(TestCase):
    """
    Class to test ServiceArea model.
    python manage.py test apps.providers.tests.models.TestServiceArea --keepdb
    """

    @classmethod
    def setUpTestData(cls):
        Provider.objects.create(
            name=PROVIDER_1,
            email=EMAIL_1,
            phone=PHONE_NUMBER_1,
            language=LANGUAGE_1,
            currency=CURRENCY_1,
        )

    def setUp(self):
        ServiceArea.objects.create(
            provider=Provider.objects.get(name=PROVIDER_1),
            name=SERVICE_AREA_1,
            price=PRICE_1,
            polygon=POLYGON_1,
        )
        ServiceArea.objects.create(
            provider=Provider.objects.get(name=PROVIDER_1),
            name=SERVICE_AREA_2,
            price=PRICE_2,
            polygon=POLYGON_2,
        )

    def test_string_representation(self):
        service_area_1 = ServiceArea.objects.get(name=SERVICE_AREA_1)

        expected_string = SERVICE_AREA_1
        received_string = str(service_area_1)
        self.assertEqual(expected_string, received_string)

    def test_get_formatted_price(self):
        expected_value = PRICE_1
        service_area_1 = ServiceArea.objects.get(name=SERVICE_AREA_1)
        received_value = service_area_1.get_formatted_price()

        self.assertEqual(expected_value, received_value)

