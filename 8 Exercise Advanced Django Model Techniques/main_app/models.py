from django.core.validators import MinValueValidator
from django.db import models
from main_app.validators import validate_only_letters_and_spaces, validate_phone_number


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            validate_only_letters_and_spaces
        ]

    )
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(18, "Age must be greater than 18")
        ]
    )
    email = models.EmailField(
        error_messages={
            'invalid': 'Enter a valid email address'
        }
    )
    phone_number = models.CharField(
        max_length=13,
        validators=[
            validate_phone_number,
        ]
    )
    website_url = models.URLField(
        error_messages={
            'invalid': "Enter a valid URL"
        }
    )
