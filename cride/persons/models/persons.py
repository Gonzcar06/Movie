"""Person model."""

# Django
from tabnanny import verbose
from django.db import models

# Utilities
from cride.utils.models import MoviesModel

class Person(MoviesModel):

    first_name=models.CharField(max_length=140)
    last_name=models.CharField(max_length=140)
    aliases = models.SlugField(unique=True, max_length=40)
    gender = models.CharField(default=True,choices=(('M', 'Male'), ('F', 'Female')),max_length=20)



