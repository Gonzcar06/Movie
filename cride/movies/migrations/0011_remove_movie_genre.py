# Generated by Django 3.2.15 on 2022-09-09 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20220908_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
    ]
