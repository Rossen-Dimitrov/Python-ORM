import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from typing import List
from main_app.models import ArtworkGallery, Laptop, ChessPlayer
from django.db.models import Case, When, Value, F


# Task 1
def show_highest_rated_art():
    best_art = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{best_art.art_name} is the highest-rated art with a {best_art.rating} rating!"


def bulk_create_arts(first_art, second_art):
    to_save_list = [first_art, second_art]
    ArtworkGallery.objects.bulk_create(to_save_list)


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# Task 2
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


# Task 3
def bulk_create_chess_players(*args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players() -> None:
    default_title = ChessPlayer._meta.get_field("title").default
    ChessPlayer.objects.filter(title=default_title).delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost():
    default_title = ChessPlayer._meta.get_field('title').default
    ChessPlayer.objects.filter(title=default_title).update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title='IM')


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title='FM')


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title='regular player')

# Task 4
