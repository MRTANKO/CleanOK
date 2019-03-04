"""Валидаторы приложения services."""
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_price(value):
    """Проверяет валидность минимальной цены."""
    if value <= 0:
        raise ValidationError(
            _('%(value)s некоректная цена'),
            params={'value': value},
        )


def validate_phone(value):
    """Проверяет валидность номера телефона."""
    if not re.fullmatch(
            r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', value):
        raise ValidationError(
            _('%(value)s некоректный номер телефона'),
            params={'value': value},
        )
