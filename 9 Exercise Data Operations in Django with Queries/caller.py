import os
import django

from populate_db import populate_model_with_data

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task


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

def apply_discount():
    all_cars = Car.objects.all()
    for car in all_cars:
        discount = sum(int(x) for x in str(car.year)) / 100
        car.price_with_discount = float(car.price) - (float(car.price) * discount)
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values("model", "price_with_discount")


def delete_last_car():
    Car.objects.last().delete()


# Car.objects.create(model='Mercedes C63 AMG', year=2019, color='white', price=120000.00)
# Car.objects.create(model='Audi Q7 S line', year=2023, color='black', price=183900.00)
# Car.objects.create(model='Chevrolet Corvette', year=2021, color='dark grey', price=199999.00)

# apply_discount()
# print(get_recent_cars())
# price_with_discount()


def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=False)
    return '\n'.join(str(x) for x in unfinished_tasks)


# print(show_unfinished_tasks())


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()

# complete_odd_tasks()

def encode_and_replace(text: str, task_title: str):
    matching_tasks = Task.objects.filter

# task = Task.objects.create(
#     title='Sample Task',
#     description='This is a sample task description',
#     due_date='2023-10-31',
#     is_finished=False,
)