# Generated by Django 4.2.4 on 2023-11-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_song_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='songs',
            field=models.ManyToManyField(related_name='artists', to='main_app.song'),
        ),
    ]
