from django.contrib.gis.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField
from decimal import Decimal

from .validators import phone_validators, ALPHANUMERIC_EXTENDED
from django.conf.global_settings import LANGUAGES, LANGUAGE_CODE
from djmoney.settings import CURRENCY_CHOICES


class Provider(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, validators=[ALPHANUMERIC_EXTENDED, ])
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=16, validators=phone_validators)
    language = models.CharField(max_length=8, default=LANGUAGE_CODE, choices=LANGUAGES)
    currency = models.CharField(max_length=4, choices=CURRENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('view_provider', args=[str(self.id)])

    def __str__(self):
        return f"{self.name}"


class ServiceArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.ForeignKey(Provider, models.DO_NOTHING, db_column='provider', blank=True, null=True)
    name = models.CharField(max_length=128, validators=[ALPHANUMERIC_EXTENDED, ])
    price = MoneyField(max_digits=19, decimal_places=4, default_currency='USD')
    polygon = models.PolygonField(geography=True, srid=4326)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('view_service_area', args=[str(self.id)])

    def get_formatted_price(self) -> Decimal:
        return self.price.amount.quantize(Decimal("0.00"))

    def __str__(self):
        return f"{self.name}"

