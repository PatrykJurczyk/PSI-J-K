# Generated by Django 4.0.1 on 2022-01-27 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_producent_image_alter_gra_opis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gra',
            name='idUzytkownika',
        ),
    ]
