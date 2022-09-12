"""Movies views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Permissions
from rest_framework import permissions

# Serializers
from cride.movies.serializers import MovieModelSerializer

# Models
from cride.movies.models import Movie

from django.core.exceptions import ValidationError


class MoviesViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Movies view set."""

    serializer_class = MovieModelSerializer
    lookup_field='title'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = (permissions.AllowAny,)
        if self.action in ['partial_update', 'update']:
            self.permission_classes = (permissions.IsAuthenticated,)
        return [p () for p in self.permission_classes]

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Movie.objects.all()
        return queryset

    def perform_create(self, serializer):
        movie = serializer.save()
        return movie
        
