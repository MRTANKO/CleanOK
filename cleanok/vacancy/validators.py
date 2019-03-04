"""Валидаторы приложения vacancy."""
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_salary(value):
    """Проверяет валидность зарплаты."""
    if value <= 0:
        raise ValidationError(
            _('%(value)s некоректная зарплата'),
            params={'value': value},
        )
