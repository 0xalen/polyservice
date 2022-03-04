from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from decimal import Decimal
from django.contrib.gis.geos import LinearRing, Polygon

"""
Dataset for testing. Centralized here in order to standardize attributes of created objects and minimize errors.   
"""

ID_1 = 1
INVALID_OBJECT_ID = 0
PROVIDER = "Provider"
PROVIDER_1 = "Provider 1"
PROVIDER_2 = "Provider 2"
CURRENCY_1 = "USD"
CURRENCY_2 = "EUR"
LANGUAGE_1 = "en"
LANGUAGE_2 = "en-gb"
EMAIL_1 = "provider1@email.fake"
EMAIL_2 = "provider2@email.fake"
PHONE_NUMBER_1 = "+1100200301"
PHONE_NUMBER_2 = "+1100200302"
SERVICE_AREA = "Service area"
SERVICE_AREA_1 = "Service area 1"
SERVICE_AREA_2 = "Service area 2"
SERVICE_AREA_3 = "Service area 3"
PRICE_1 = Decimal('01.05')
PRICE_2 = Decimal('02.15')
PRICE_3 = Decimal('03.30')
POLYGON_1 = Polygon(((1, 0), (2, 2), (2, 0), (1, 0)), ((0.5, 0), (1.5, 0.5), (0.5, 0.5), (0.5, 0)))
POLYGON_2 = Polygon(((5, 0), (3, 2), (3, 4), (5, 0)), ((4.5, 0), (2.5, 0.5), (2.5, 0.5), (4.5, 0)))
POLYGON_3 = Polygon(((6, 0), (7, 2), (6, 4), (6, 0)), ((5.5, 5), (3.5, 3.5), (4.5, 3.5), (5.5, 5)))
API_USER = "apiuser"
API_USER_PASSWORD = "password"


class TestProvidersUrlsBase(TestCase):
    """
    Base class with urls used by the providers app.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url_provider_detail = reverse('providers:provider_detail', kwargs={'pk': ID_1})
        cls.url_provider_update = reverse('providers:provider_update', kwargs={'pk': ID_1})
        cls.url_provider_delete = reverse('providers:provider_delete', kwargs={'pk': ID_1})
        cls.url_provider_create = reverse('providers:provider_create')
        cls.url_provider_list = reverse('providers:provider_list')

        cls.url_service_area_detail = reverse('providers:service_area_detail', kwargs={'pk': ID_1})
        cls.url_service_area_delete = reverse('providers:service_area_delete', kwargs={'pk': ID_1})
        cls.url_service_area_update = reverse('providers:service_area_update', kwargs={'pk': ID_1})
        cls.url_service_area_create = reverse('providers:service_area_create')
        cls.url_service_area_list = reverse('providers:service_area_list')
