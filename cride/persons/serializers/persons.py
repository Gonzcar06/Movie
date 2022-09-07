"""Movies serializers."""

# Django REST Framework
from rest_framework import serializers

# Serializers
from cride.movies.serializers import MovieModelSerializer

# Model
from cride.persons.models import Person, Actor, MaleActor, FemaleActor
                                

class PersonModelSerializer(serializers.ModelSerializer):
    """Person model serializer."""

    class Meta:
        """Meta class."""

        model = Actor
        fields = (
            'id', 'last_name', 'first_name',
            'aliases', 'gender', 'p_actor', 'p_director' ,'p_productor',
        )   
        depth = 1
       