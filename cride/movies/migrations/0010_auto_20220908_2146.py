# Generated by Django 3.2.15 on 2022-09-08 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20220908_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selectgenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.CharField(max_length=100)),
                ('s_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Genress',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_type',
            field=models.ManyToManyField(to='movies.Selectgenre'),
        ),
    ]
