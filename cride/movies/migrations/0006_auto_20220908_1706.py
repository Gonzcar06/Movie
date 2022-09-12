# Generated by Django 3.2.15 on 2022-09-08 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
        ('movies', '0005_alter_roles_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roles',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.person'),
        ),
    ]