"""Persons views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Serializers
from cride.persons.serializers import (
    PersonModelSerializer,
)

# Models
from cride.persons.models import Person


class PersonViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Person view set."""

    #queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    lookup_field='first_name'

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Person.objects.all()
        return queryset
    
    def perform_create(self, serializer):
        person = serializer.save()
        return person

