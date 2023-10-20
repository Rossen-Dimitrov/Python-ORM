from datetime import date

from django.db import models

CITIES = [
    ("Sofia", "Sofia"),
    ("Plovdiv", "Plovdiv"),
    ("Burgas", "Burgas"),
    ("Varna", "Varna"),
]


class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_text = models.TextField()


class Employee(models.Model):
    name = models.CharField(
        max_length=30
    )
    email_address = models.EmailField(
        editable=False
    )
    photo = models.URLField(
        default='http:/default.url/image.png',
        blank=True
    )
    birth_date = models.DateField(
        null=True,
        blank=True
    )
    works_full_time = models.BooleanField
    created_on = models.DateTimeField(
        auto_now_add=True
    )


class Department(models.Model):
    code = models.CharField(
        max_length=4,
        primary_key=True,
        unique=True)
    name = models.CharField(
        max_length=50,
        unique=True)
    employees_count = models.PositiveIntegerField(
        default=1,
        verbose_name="Employees Count")
    location = models.CharField(
        max_length=20, choices=CITIES,
        null=True,
        blank=True)
    last_edited_on = models.DateTimeField(
        auto_now=True,
        editable=False)


class Project(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True)
    description = models.TextField(
        null=False,
        blank=True)
    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=False
    )
    duration_in_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Duration in Days")
    estimated_hours = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Estimated Hours")
    start_date = models.DateField(
        null=True,
        blank=True,
        default=date.today,
        verbose_name="Start Date")
    created_on = models.DateField(
        auto_now=True,
        editable=False)
    last_edited_on = models.DateTimeField(
        auto_now_add=True,
        editable=False)
