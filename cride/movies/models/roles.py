"""Role model."""

# Django
from django.db import models

# Utilities
from cride.movies.models import Movie
from cride.persons.models import Person

ROLE_TYPES = (
    ('Director', 'Director'),
    ('Actor', 'Actor'),
    ('Producer', 'Producer'),
)

class Role(Movie):
    movie = models.ForeignKey(Movie, related_name="roles",on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name="roles",on_delete=models.CASCADE)
    role_type = models.CharField(max_length=100,choices=ROLE_TYPES)
    role_name = models.CharField(max_length=100)