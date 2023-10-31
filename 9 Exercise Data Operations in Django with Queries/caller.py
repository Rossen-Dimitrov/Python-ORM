import os
import django

from populate_db import populate_model_with_data

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


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
    decoded_text = ''.join(chr(ord(x) - 3) for x in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)
    # matching_tasks = Task.objects.filter(title=task_title)
    # decoded_text = ''.join(chr(ord(x) - 3) for x in text)
    # for task in matching_tasks:
    #     task.description = decoded_text
    #     task.save()


# task = Task.objects.create(
#     title='Sample Task',
#     description='This is a sample task description',
#     due_date='2023-10-31',
#     is_finished=False,
# )

# encode_and_replace("Zdvk#wkh#glvkhv$", "Sample Task")

def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    rooms_list = []
    for room in deluxe_rooms:
        if room.id % 2 == 0:
            rooms_list.append(str(room))

    return ''.join(rooms_list)


def increase_room_capacity():
    all_rooms = HotelRoom.objects.all().order_by('id')
    previous_room_capacity = None
    for room in all_rooms:
        if not room.is_reserved:
            continue
        if not previous_room_capacity:
            room.capacity += room.id
        else:
            room.capacity += previous_room_capacity

        previous_room_capacity = room.capacity
        room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if last_room.is_reserved:
        last_room.delete()


# task = HotelRoom.objects.create(
#     room_number=101,
#     room_type='Standard',
#     capacity=2,
#     amenities='Tv',
#     price_per_night=100.00,
# )
# task1 = HotelRoom.objects.create(
#     room_number=201,
#     room_type='Deluxe',
#     capacity=3,
#     amenities='Wi-Fi',
#     price_per_night=200.00,
# )
# task2 = HotelRoom.objects.create(
#     room_number=501,
#     room_type='Deluxe',
#     capacity=6,
#     amenities='Jacuzzi',
#     price_per_night=400.00,
# )


def update_characters():
    all_characters = Character.objects.all()
    for character in all_characters:
        if character.class_name == "Mage":
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == "Warrior":
            character.hit_points /= 2
            character.dexterity += 4
        elif character.class_name in ["Assassin", "Scout"]:
            character.inventory = "The inventory is empty"
        character.save()


def fuse_characters(first_character: Character, second_character: Character):
    if first_character.class_name in ["Mage", "Scout"]:
        char_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        char_inventory = "Dragon Scale Armor, Excalibur"
    Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=int((first_character.level + second_character.level) // 2),
        strength=int((first_character.strength + second_character.strength) * 1.2),
        dexterity=int((first_character.dexterity + second_character.dexterity) * 1.4),
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=(first_character.hit_points + second_character.hit_points),
        inventory=char_inventory,
    )


def grand_dexterity():
    for char in Character.objects.all():
        char.dexterity = 30
        char.save()


def grand_intelligence():
    for char in Character.objects.all():
        char.intelligence = 40
        char.save()


def grand_strength():
    for char in Character.objects.all():
        char.strength = 50
        char.save()


def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()

#
# character1 = Character.objects.create(
#     name="Gandalf",
#     class_name="Mage",
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory="Staff of Magic, Spellbook",
# )
#
# character2 = Character.objects.create(
#     name="Hector",
#     class_name="Warrior",
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory="Sword of Troy, Shield of Protection",
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
