# Generated by Django 4.2.4 on 2023-10-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_set_price_and_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('customer_name', models.CharField(max_length=100)),
                ('order_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=20)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('warranty', models.CharField(default='No warranty', max_length=100)),
                ('delivery', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
