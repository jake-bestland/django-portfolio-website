# Generated by Django 5.1.2 on 2024-11-19 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SpotifyToken',
        ),
    ]
