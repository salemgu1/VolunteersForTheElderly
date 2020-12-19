# Generated by Django 3.0.2 on 2020-12-19 14:14

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_mymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
