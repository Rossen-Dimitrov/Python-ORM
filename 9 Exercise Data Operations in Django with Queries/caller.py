import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location


def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species)

    return f"{name} is a very cute {species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))

def create_artifact(
        name: str,
        origin: str,
        age: int,
        description: str,
        is_magical: bool
):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact(
#     'Ancient Sword','Lost Kingdom', 500,
#     'A legendary sword with a rich history', True))
# print(create_artifact(
#     'Crystal Amulet', 'Mystic Forest', 300,
#     'A magical amulet believed to bring good fortune', True))
# print(create_artifact(
#     'Stone Tablet', 'Ruined Temple', 1000,
#     'An ancient tablet covered in mysterious inscriptions',False))

def show_all_locations():
    locations = Location.objects.all().order_by(id)
    for location in locations:
        return f"{location.name} has a population of {location.population}!"


def new_capital():
    capital = Location.objects.first()
    capital.is_capital = True
    capital.save()
    