# Generated by Django 5.1.2 on 2024-11-19 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_project_animated_gif_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['name']},
        ),
    ]
