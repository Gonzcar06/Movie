"""Role model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import MoviesModel


class Genre(MoviesModel):
    #s_movie = models.ForeignKey('movies.Movie',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

def __str__(self):
    return self.name
