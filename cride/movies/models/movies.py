"""Movie model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import MoviesModel
from cride.persons.models import Person


class Movie(MoviesModel):
    title = models.CharField('movie title', max_length=140)
    #genre = models.CharField(max_length=140)
    #genre_type = models.CharField(max_length=140)
    genre_t=models.OneToOneField('movies.Genre', on_delete=models.CASCADE,default=False)
    release_year = models.PositiveIntegerField(default=0)
    casting = models.ManyToManyField(
        'persons.Person',
        through='movies.Roles',
        through_fields=('movie', 'person'),
        blank=True
    )

    


  

