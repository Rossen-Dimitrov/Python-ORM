import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, F
from main_app.models import Profile, Product, Order


def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ""

    query = (Q(full_name__icontains=search_string) |
             Q(email__icontains=search_string) |
             Q(phone_number__icontains=search_string))

    profiles = Profile.objects.filter(query).order_by('full_name')

    all_profiles = []
    for p in profiles:
        all_profiles.append(
            f"Profile: {p.full_name},"
            f" email: {p.email},"
            f" phone number: {p.phone_number},"
            f" orders: {p.orders.count()}")

    return '\n'.join(all_profiles)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    return '\n'.join(f"Profile: {p.full_name}, orders: {p.count_orders}" for p in profiles)


def get_last_sold_products():
    last_order = Order.objects.prefetch_related('products').last()

    if last_order is None or not last_order.products.exists():
        return ""

    products = [p.name for p in last_order.products.all()]

    return f"Last sold products: {', '.join(products)}"


def get_top_products():
    top_product = ((Product.objects.annotate(
        orders_count=Count('ordered_products')
    ).filter(orders_count__gt=0)
                    ).order_by(
        '-orders_count', 'name')
                  )[:5]

    if not top_product:
        return ""
    result = [f"{p.name}, sold {p.orders_count} times" for p in top_product]
    return f"Top products:\n" + '\n'.join(result)


def apply_discounts():
    updated_count = Order.objects.annotate(
        products_count=Count('products')
    ).filter(
        products_count__gt=2,
        is_completed=False,
    ).update(
        total_price=F('total_price') * 0.90
    )

    return f"Discount applied to {updated_count} orders."


def complete_order():
    oldest_order = Order.objects.prefetch_related('products').first()
    products = oldest_order.products.values_list('name', flat=True)

    for p in products:
        print(p)

complete_order()
