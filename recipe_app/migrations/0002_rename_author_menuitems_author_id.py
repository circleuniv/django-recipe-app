# Generated by Django 5.0.10 on 2025-01-06 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitems',
            old_name='author',
            new_name='author_id',
        ),
    ]