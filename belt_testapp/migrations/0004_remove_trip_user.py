# Generated by Django 2.2 on 2020-04-27 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_testapp', '0003_auto_20200426_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
    ]
