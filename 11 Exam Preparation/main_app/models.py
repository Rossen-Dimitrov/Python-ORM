from django.core import validators
from django.db import models


# Create your models here.

class Person(models.Model):
    full_name = models.CharField(
        max_length=120,
        validators=[
            validators.MinLengthValidator(2),
        ]
    )

    birth_date = models.DateField(
        default='1900-01-01',
    )

    nationality = models.CharField(
        max_length=50,
        default='Unknown',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.full_name


class Director(Person):
    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=[
            validators.MinValueValidator(0),
        ]
    )


class Actor(Person):
    is_awarded = models.BooleanField(
        default=False,
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )


class Movie(models.Model):
    class GenreChoices(models.TextChoices):
        ACTION = 'Action',
        COMEDY = 'Comedy',
        DRAMA = 'Drama',
        OTHER = 'Other',

    title = models.CharField(
        max_length=150,
        validators=[
            validators.MinLengthValidator(5),
        ]
    )
    release_date = models.DateField()
    storyline = models.TextField(
        blank=True,
        null=True,
    )
    genre = models.CharField(
        max_length=6,
        choices=GenreChoices.choices,
        default=GenreChoices.OTHER,
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
        validators=(
            validators.MinValueValidator(0.0),
            validators.MaxValueValidator(10.0),
        )

    )
    is_classic = models.BooleanField(
        default=False,
    )
    is_awarded = models.BooleanField(
        default=False,
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )
    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name='director_movies'
    )
    starring_actor = models.ForeignKey(
        to=Actor,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='starring_movies',
    )
    actors = models.ManyToManyField(
        to=Actor,
        related_name='actor_movies',
    )
