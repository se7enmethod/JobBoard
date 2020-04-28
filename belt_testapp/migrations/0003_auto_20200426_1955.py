# Generated by Django 2.2 on 2020-04-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_testapp', '0002_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ManyToManyField(related_name='trips', to='belt_testapp.User'),
        ),
    ]