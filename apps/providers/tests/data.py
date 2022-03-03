from decimal import Decimal

from django.contrib.gis.geos import LinearRing, Polygon

PROVIDER_1 = "Provider 1"
PROVIDER_2 = "Provider 2"
CURRENCY_1 = "USD"
CURRENCY_2 = "EUR"
LANGUAGE_1 = "en-us"
LANGUAGE_2 = "en-gb"
EMAIL_1 = "provider1@email.fake"
EMAIL_2 = "provider2@email.fake"
PHONE_NUMBER_1 = "+1100200301"
PHONE_NUMBER_2 = "+1100200302"
SERVICE_AREA_1 = "Service area 1"
SERVICE_AREA_2 = "Service area 2"
PRICE_1 = Decimal('01.05')
PRICE_2 = Decimal('02.15')
POLYGON_1 = Polygon(((1, 0), (2, 2), (2, 0), (1, 0)), ((0.5, 0), (1.5, 0.5), (0.5, 0.5), (0.5, 0)))
POLYGON_2 = Polygon(((5, 0), (3, 2), (3, 4), (5, 0)), ((4.5, 0), (2.5, 0.5), (2.5, 0.5), (4.5, 0)))
