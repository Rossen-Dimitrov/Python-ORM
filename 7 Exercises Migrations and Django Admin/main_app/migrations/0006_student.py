# Generated by Django 4.2.4 on 2023-10-24 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('grade', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
