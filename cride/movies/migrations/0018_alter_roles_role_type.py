# Generated by Django 3.2.15 on 2022-09-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_alter_movie_genre_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='role_type',
            field=models.CharField(choices=[('Director', 'Director'), ('Actor', 'Actor'), ('Producer', 'Producer')], default='Actor', max_length=100),
        ),
    ]
