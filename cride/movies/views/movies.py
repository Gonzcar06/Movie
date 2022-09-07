"""Movies views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Serializers
from cride.movies.serializers import MovieModelSerializer

# Models
from cride.movies.models import Movie


class MoviesViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Movies view set."""

    serializer_class = MovieModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Movie.objects.all()
        return queryset