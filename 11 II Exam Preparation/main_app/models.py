from django.core import validators
from django.db import models


class CreationDate(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField(
        auto_now_add=True
    )


class Profile(CreationDate):
    full_name = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(2),
        ]
    )
    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15,
    )
    address = models.TextField()

    is_active = models.BooleanField(
        default=True,
    )


class Product(CreationDate):
    name = models.CharField(
        max_length=100,
    )
    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(0.01),
        ]
    )
    in_stock = models.PositiveIntegerField()

    is_available = models.BooleanField(
        default=True,
    )


class Order(CreationDate):
    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name='orders',
    )
    products = models.ManyToManyField(
        to=Product,
        related_name='ordered_products',
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            validators.MinValueValidator(0.01),
        ]
    )
    is_completed = models.BooleanField(
        default=False,
    )
