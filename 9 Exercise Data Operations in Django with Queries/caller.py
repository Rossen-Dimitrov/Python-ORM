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
    locations = Location.objects.all().order_by('-id')

    return '\n'.join(str(x) for x in locations)


def new_capital():
    Location.objects.filter(pk=1).update(is_capital=True)
    # capital = Location.objects.first()
    # capital.is_capital = True
    # capital.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()

# location = Location.objects.create(
#     name='Sofia', region='Sofia Region', population=1329000,
#     description='The capital of Bulgaria and the largest city in the country', is_capital=False
# )
#
# location1 = Location.objects.create(
#     name='Plovdiv', region='Plovdiv Region', population=346942,
#     description='The second-largest city in Bulgaria with a rich historical heritage', is_capital=False
# )
#
# location2 = Location.objects.create(
#     name='Varna', region='Varna Region', population=330486,
#     description='A city known for its sea breeze and beautiful beaches on the Black Sea', is_capital=False
# )

# print(show_all_locations())
# print(new_capital())
# print(get_capitals())
