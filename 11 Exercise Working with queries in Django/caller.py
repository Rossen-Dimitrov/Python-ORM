import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from typing import List
from main_app.models import ArtworkGallery, Laptop
from django.db.models import Case, When, Value, F


def show_highest_rated_art():
    best_art = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{best_art.art_name} is the highest-rated art with a {best_art.rating} rating!"


def bulk_create_arts(first_art, second_art):
    to_save_list = [first_art, second_art]
    ArtworkGallery.objects.bulk_create(to_save_list)


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop() -> str:
    most_expensive = Laptop.objects.order_by("-price", "id").first()

    return f"{most_expensive.brand} is the most expensive laptop available for {most_expensive.price}$!"


def bulk_create_laptops(*args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(
        brand__in=["Asus", "Lenovo"]
    ).update(storage=512)
    # Laptop.objects.filter(
    # Q(brand="Lenovo") | Q(brand="Asus")
    # ).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(
        brand__in=["Apple", "Dell", "Acer"]
    ).update(memory=16)


def update_operation_systems():
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value("Windows")),
            When(brand="Apple", then=Value("MacOS")),
            When(brand__in=["Dell", "Acer"], then=Value("Linux")),
            When(brand="Lenovo", then=Value("Chrome OS")),
            default=F('operation_system')
        )
    )

    # Laptop.objects.filter(brand="Asus").update(operation_system="Windows")
    # Laptop.objects.filter(brand="Apple").update(operation_system="MacOS")
    # Laptop.objects.filter(brand__in=["Dell", "Acer"]).update(operation_system="Linux")
    # Laptop.objects.filter(brand="Lenovo").update(operation_system="Chrome OS")


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()




