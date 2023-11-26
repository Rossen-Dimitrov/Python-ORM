from django.core import validators
from django.db import models

from main_app.managers import AuthorManager


class Author(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[
            validators.MinLengthValidator(2),
        ]
    )
    email = models.EmailField(
        unique=True,
    )
    is_banned = models.BooleanField(
        default=False,
    )
    birth_year = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(1900),
            validators.MaxValueValidator(2005),
        ]
    )
    website = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.full_name

    objects = AuthorManager()


class Article(models.Model):
    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = 'Technology',
        SCIENCE = 'Science',
        EDUCATION = 'Education',

    title = models.CharField(
        max_length=200,
        validators=[
            validators.MinLengthValidator(5),
        ]
    )
    content = models.TextField(
        validators=[
            validators.MinLengthValidator(10),
        ]
    )
    category = models.CharField(
        max_length=10,
        choices=CategoryChoices.choices,
        default=CategoryChoices.TECHNOLOGY,
    )

    authors = models.ManyToManyField(
        to=Author,
        related_name='articles'
    )
    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField(
        validators=[
            validators.MinLengthValidator(10),
        ]
    )
    rating = models.FloatField(
        validators=[
            validators.MinValueValidator(1.0),
            validators.MaxValueValidator(5.0),
        ]
    )
    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
