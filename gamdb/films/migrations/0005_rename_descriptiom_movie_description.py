# Generated by Django 4.1.7 on 2023-03-28 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_alter_movie_genres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='descriptiom',
            new_name='description',
        ),
    ]