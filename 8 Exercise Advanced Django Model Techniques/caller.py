import os
from decimal import Decimal

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.core.exceptions import ValidationError
from main_app.models import Book, Product, DiscountedProduct, SpiderHero, FlashHero, Document

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


# # Create a Product instance
# product = Product.objects.create(name="Gaming Keyboard", price=Decimal(100.00))
#
# # Calculate and print the tax
# tax_price = product.calculate_tax()
# print(f"Tax for {product.name}: ${tax_price:.2f}")
#
# # Calculate and print the shipping cost
# shipping_cost = product.calculate_shipping_cost(Decimal(2.50))
# print(f"Shipping Cost for {product.name}: ${shipping_cost:.2f}")
#
# # Format and print the product name
# formatted_name = product.format_product_name()
# print(f"Formatted Product Name: {formatted_name}")
#
# # Create a DiscountedProduct instance
# discounted_product = DiscountedProduct.objects.create(name="Gaming Mouse", price=Decimal(120.00))
#
# # Calculate and print the price without discount (DiscountedProduct)
# discounted_price = discounted_product.calculate_price_without_discount()
# print(f"Price Without Discount for {discounted_product.name}: ${discounted_price:.2f}")
#
# # Calculate and print the tax (DiscountedProduct)
# tax_price = discounted_product.calculate_tax()
# print(f"Tax for {discounted_product.name}: ${tax_price:.2f}")
#
# # Calculate and print the shipping cost (DiscountedProduct)
# shipping_cost = discounted_product.calculate_shipping_cost(Decimal(2.50))
# print(f"Shipping Cost for {discounted_product.name}: ${shipping_cost:.2f}")
#
# # Format and print the product name (DiscountedProduct)
# formatted_name = discounted_product.format_product_name()
# print(f"Formatted Product Name: {formatted_name}")


# Create instance of SpiderHero
# spiderman = SpiderHero(name="Spider-Man", hero_title="Spider Hero", energy=100)
# # Create instance of FlashHero
# flash = FlashHero(name="The Flash", hero_title="Flash Hero", energy=70)
#
# # Save the instances to the database
# spiderman.save()
# flash.save()
#
# # Run the special abilities
# print(spiderman.swing_from_buildings())
# print(flash.run_at_super_speed())
# print(spiderman.swing_from_buildings())
#
# # Recharge the energy of Spider-Man and The Flash using the mixin method
# spiderman.recharge_energy(195)
# flash.recharge_energy(40)
#
# # Now you can check the updated energy levels
# print(f"{spiderman.name} - Energy: {spiderman.energy}")
# print(f"{flash.name} - Energy: {flash.energy}")


from django.contrib.postgres.search import SearchVector

# Create the first 'Document' object with a title and content.
document1 = Document.objects.create(
    title="Django Framework 1",
    content="Django is a high-level Python web framework for building web applications.",
)

# Create the second 'Document' object with a title and content.
document2 = Document.objects.create(
    title="Django Framework 2",
    content="Django framework provides tools for creating web pages, handling URL routing, and more.",
)

# Update the 'search_vector' field in the 'Document' model with search vectors.
Document.objects.update(search_vector=SearchVector('title', 'content'))

# Perform a full-text search for documents containing the words 'django' and 'web framework'.
results = Document.objects.filter(search_vector='django web framework')

# Print the search results.
for result in results:
    print(f"Title: {result.title}")