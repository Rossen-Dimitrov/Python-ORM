# Generated by Django 4.2.4 on 2023-11-13 11:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_movie_options_alter_music_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6, 'ISBN must be at least 6 characters long')]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(8, 'Director must be at least 8 characters long')]),
        ),
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(9, 'Artist must be at least 9 characters long')]),
        ),
    ]
