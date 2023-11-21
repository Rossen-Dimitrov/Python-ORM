from django.db import models


class ProfileManger(models.Manager):
    def get_regular_customers(self):
        return (self.annotate(
            count_orders=models.Count("orders"))
                .filter(count_orders__gt=2)
                .order_by('-count_orders')
        )
