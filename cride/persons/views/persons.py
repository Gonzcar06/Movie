"""Persons views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from cride.persons.serializers import (
    PersonModelSerializer,
    #PersonCreateSerializer,
)

from cride.movies.serializers import MovieModelSerializer

# Models
from cride.persons.models import Person
from cride.movies.models import Movie


class PersonViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Person view set."""

    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Person.objects.all()
        return queryset
    
    def perform_create(self, serializer):
        person = serializer.save()
        return person

    