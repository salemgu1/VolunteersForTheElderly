# Generated by Django 3.0.2 on 2020-12-19 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_mymodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='phone_number',
        ),
    ]