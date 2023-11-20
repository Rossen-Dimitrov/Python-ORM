from django.db import models

# Create your models here.
class Director(models.Model):
    full_name = models.
    birth_date = models.
    nationality = models.
    years_of_experience = models.
class Actor(Director):
    full_name = models.
    birth_date = models.
    nationality = models.
    is_awarded = models.
    last_updated = models.
class Movie(models.Model):
    title = models.
    release_date = models.
    storyline = models.
    genre = models.
    rating = models.
    is_classic = models.
    is_awarded = models.
    last_updated = models.
    director = models.
    starring_actor = models.
    actors = models.
