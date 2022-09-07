"""Person model."""

# Django
from tabnanny import verbose
from django.db import models

# Utilities
from cride.utils.models import MoviesModel
#from cride.movies.models import Movie

class Person(MoviesModel):

    # Name
    first_name=models.CharField(max_length=140)
    last_name=models.CharField(max_length=140)
    aliases = models.SlugField(unique=True, max_length=40)
    gender = models.CharField(default=True,choices=(('M', 'Male'), ('F', 'Female')),max_length=20)
    p_actor = models.BooleanField(default=False)
    p_director = models.BooleanField(default=False) 
    p_productor = models.BooleanField(default=False) 

    def __str__(self):
        """Return Person name."""   
        return self.first_name


class Actor(Person):
    class Meta:
        verbose_name = "Actor"  

class MaleActorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender='M')

class MaleActor(Actor):
    objects = MaleActorManager
    class Meta:
        proxy=True

    def __str__(self):
        """Return Person name."""   
        return self.objects

class FemaleActorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender='F')

class FemaleActor(Actor):
    objects = FemaleActorManager
    class Meta:
        proxy=True
        
    def __str__(self):
        """Return Person name."""   
        return self.objects
    
class Director(Person):
    class Meta:
        verbose_name = "Director"

class Producer(Person):
    class Meta:
        verbose_name = "Producer"
   