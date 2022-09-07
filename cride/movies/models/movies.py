"""Movie model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import MoviesModel

from cride.persons.models import Person


class Movie(MoviesModel):
    title = models.CharField('movie title', max_length=140)
    genre = models.CharField(max_length=140)
    release_year = models.PositiveIntegerField(default=0)
    casting = models.ManyToManyField(
        to=Person,
        through='movies.Role',
        through_fields=('movie_id', 'person_id')
    )


  

