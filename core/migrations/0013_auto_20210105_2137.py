# Generated by Django 3.0.2 on 2021-01-05 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('זכר', 'זכר'), ('נקבה', 'נקבה')], default='זכר', max_length=10),
        ),
    ]
