"""Movies serializers."""

# Django REST Framework
from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response

# Serializers
from cride.movies.serializers import RoleModelSerializerForPerson

# Model
from cride.persons.models import Person
                                

class PersonModelSerializer(serializers.HyperlinkedModelSerializer):
    """Person model serializer."""
    url = serializers.HyperlinkedIdentityField(view_name="persons:persons-detail", lookup_field='first_name', read_only=True)
    roles = RoleModelSerializerForPerson(many=True)
    
    class Meta:
        """Meta class."""

        model = Person
        fields = (
            'url', 
            'id', 'last_name', 'first_name',
            'aliases', 'gender', 
            'roles',
        )   
        extra_kwargs = {'roles': {'required': False}}


    #def create(self, data):
    #    person = Person.objects.create_user(**data)
    #    return person

       