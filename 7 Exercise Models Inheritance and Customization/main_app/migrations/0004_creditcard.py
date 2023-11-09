# Generated by Django 4.2.4 on 2023-11-09 10:55

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_owner', models.CharField(max_length=100)),
                ('card_number', main_app.models.MaskedCreditCardField()),
            ],
        ),
    ]
