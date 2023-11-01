import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from typing import List
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon
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

def set_new_chefs() -> None:
    Meal.objects.update(
        chef=Case(
            When(meal_type="Breakfast", then=Value("Gordon Ramsay")),
            When(meal_type="Lunch", then=Value("Julia Child")),
            When(meal_type="Dinner", then=Value("Jamie Oliver")),
            When(meal_type="Snack", then=Value("Thomas Keller")),
            default=F('chef')
        )
    )


def set_new_preparation_times() -> None:
    Meal.objects.update(
        preparation_time=Case(
            When(meal_type="Breakfast", then=Value("10 minutes")),
            When(meal_type="Lunch", then=Value("12 minutes")),
            When(meal_type="Dinner", then=Value("15 minutes")),
            When(meal_type="Snack", then=Value("5 minutes")),
            default=F('preparation_time')
        )
    )


def update_low_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=["Breakfast", "Dinner"]).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).delete()


# Task 5

def show_hard_dungeons() -> str:
    hardest_dungeons = Dungeon.objects.filter(difficulty="Hard").order_by('-location')

    return '\n'.join(str(h) for h in hardest_dungeons)


def bulk_create_dungeons(*args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names() -> None:
    Dungeon.objects.update(
        name=Case(
            When(difficulty="Easy", then=Value("The Erased Thombs")),
            When(difficulty="Medium", then=Value("The Coral Labyrinth")),
            When(difficulty="Hard", then=Value("The Lost Haunt")),
        )
    )


def update_dungeon_bosses_health() -> None:
    Dungeon.objects.exclude(difficulty="Easy").update(boss_health=500)


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.update(
        recommended_level=Case(
            When(difficulty="Easy", then=Value(25)),
            When(difficulty="Medium", then=Value(50)),
            When(difficulty="Hard", then=Value(75)),
        )
    )


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")


def set_new_locations() -> None:
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")
