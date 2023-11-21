import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order

profile = Profile.objects.get_regular_customers()
print(profile.values_list('full_name', flat=True))


