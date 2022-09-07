"""Movie serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from cride.movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    """Movie model serializer."""

    class Meta:
        """Meta class."""

        model = Movie 
        fields = (
            'id', 'title', 'genre',
            'release_year', 'casting',
        )
        depth = 1