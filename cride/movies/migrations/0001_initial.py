# Generated by Django 3.2.15 on 2022-09-07 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('title', models.CharField(max_length=140, verbose_name='movie title')),
                ('genre', models.CharField(max_length=140)),
                ('release_year', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('movie_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='movies.movie')),
                ('role_type', models.CharField(choices=[('Director', 'Director'), ('Actor', 'Actor'), ('Producer', 'Producer')], max_length=100)),
                ('role_name', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='movies.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.person')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
            bases=('movies.movie',),
        ),
        migrations.AddField(
            model_name='movie',
            name='casting',
            field=models.ManyToManyField(through='movies.Role', to='persons.Person'),
        ),
    ]
