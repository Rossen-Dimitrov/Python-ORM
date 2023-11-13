import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.core.exceptions import ValidationError
from main_app.models import Book

# from main_app.models import Customer
#
# # Import your models here
#
# customer1 = Customer(
#     name="Svetlin Nakov",
#     age=18,
#     email="nakov@example.com",
#     phone_number="+359123456789",
#     website_url="https://judge.softuni.org/"
# )
#
# try:
#     customer1.full_clean()
#     customer1.save()
# except ValidationError as e:
#     print('\n'.join(e.messages))


# book = Book(
#     title="Short Title",
#     description="A book with a short title.",
#     genre="Fiction",
#     author="A",
#     isbn="1234"
# )
#
# try:
#     book.full_clean()
#     book.save()
#
# except ValidationError as e:
#     print("Validation Error for Book:")
#     for field, errors in e.message_dict.items():
#         print(f"{field}: {', '.join(errors)}")


