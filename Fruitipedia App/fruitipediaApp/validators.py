from django.core import exceptions


def validate_only_letters(value):
    if not all(c.isalpha() for c in value):
        raise exceptions.ValidationError("Fruit name should contain only letters!")
