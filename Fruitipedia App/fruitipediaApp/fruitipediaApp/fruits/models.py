from django.core import validators
from django.db import models

from validators import validate_only_letters


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            validators.MinLengthValidator(2),
            validate_only_letters,
        ]
    )
    Image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.CharField(
        blank=False,
        null=False,
    )
    nutrition = models.TextField(
        blank=True,
        null=True,
    )
    categories = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
