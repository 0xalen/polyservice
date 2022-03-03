from django.core.validators import RegexValidator
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator


ALPHANUMERIC = RegexValidator(
    r'^[0-9a-zA-ZñÑ]*$',
    'Only alphanumeric characters are allowed.'
)

NUMERIC = RegexValidator(
    r'^[0-9]*$',
    'Only numbers are allowed.'
)

ALPHANUMERIC_EXTENDED = RegexValidator(
    r'^([0-9a-zA-ZñÑçÇ\'\-\u00C0-\u00FF]|[\s])*$',
    'Only alphanumeric characters are allowed (with or without accents.'
)


phone_regex = RegexValidator(
    r'^\+?1?\{9-15}$',
    'Phone number should include country code and should have a length between 9 and 15 characters'
)

phone_validators = [
    phone_regex,
]

# To configure custom validation, see django-money documentation: https://django-money.readthedocs.io/en/stable/
currency_validators = [
    # MinMoneyValidator(10),
    # MaxMoneyValidator(1500),
    # MinMoneyValidator(Money(500, 'USD')),
    # MaxMoneyValidator(Money(900, 'USD')),
    # MinMoneyValidator({'EUR': 100, 'USD': 50}),
    # MaxMoneyValidator({'EUR': 1000, 'USD': 500}),
]
