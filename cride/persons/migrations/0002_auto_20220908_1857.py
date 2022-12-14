# Generated by Django 3.2.15 on 2022-09-08 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20220908_1715'),
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='person_ptr',
        ),
        migrations.RemoveField(
            model_name='director',
            name='person_ptr',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='person_ptr',
        ),
        migrations.DeleteModel(
            name='FemaleActor',
        ),
        migrations.DeleteModel(
            name='MaleActor',
        ),
        migrations.RemoveField(
            model_name='person',
            name='p_actor',
        ),
        migrations.RemoveField(
            model_name='person',
            name='p_director',
        ),
        migrations.RemoveField(
            model_name='person',
            name='p_productor',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Producer',
        ),
    ]
