"""Role model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import MoviesModel

ROLE_TYPES = (
    ('Director', 'Director'),
    ('Actor', 'Actor'),
    ('Producer', 'Producer'),
)

class Roles(MoviesModel):
    movie = models.ForeignKey('movies.Movie', related_name="roles",on_delete=models.CASCADE)
    person = models.ForeignKey('persons.Person', related_name="roles",on_delete=models.CASCADE)
    role_type = models.CharField(max_length=100,choices=ROLE_TYPES,default='Actor')
    role_name = models.CharField(max_length=100)