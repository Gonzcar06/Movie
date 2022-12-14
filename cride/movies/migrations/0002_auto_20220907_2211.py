# Generated by Django 3.2.15 on 2022-09-07 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='casting',
            field=models.ManyToManyField(related_name='made_movies', through='movies.Role', to='persons.Person'),
        ),
        migrations.AlterField(
            model_name='role',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='made_roles', to='persons.person'),
        ),
    ]
