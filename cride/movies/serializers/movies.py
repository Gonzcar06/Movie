"""Movie serializers."""

# Django REST Framework
from rest_framework import serializers
#from cride.persons.serializers import PersonModelSerializer
from cride.movies.models import Movie, Roles, Genre

class GeneredModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "name",
        )

class RoleModelSerializerForMovie(serializers.RelatedField):
    
    def to_representation(self, data):
        return {
            "first_name": data.first_name,
            "last_name" : data.last_name,  
            "aliases" : data.aliases,
            "gender" : data.gender,
        }
    


class MovieModelSerializer(serializers.HyperlinkedModelSerializer):
    """Movie model serializer."""
    url = serializers.HyperlinkedIdentityField(view_name="movies:movies-detail", lookup_field='title', read_only=True)
    casting = RoleModelSerializerForMovie(many=True, read_only=True)
    genre_t= GeneredModelSerializer(read_only=False)
    class Meta:
        """Meta class."""
        
        model = Movie
        fields = (
            "url",
            "id",
            "title",
            "genre_t",
            "release_year",
            "casting",
        )
        extra_kwargs = {'casting': {'required': False}}


    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        genre_validated_data = validated_data.pop('genre_t')
        if genre_validated_data:
            genre_obj = Genre.objects.create(movie=movie)
            genre_obj.name = genre_validated_data.get('name')
        movie.save()
        return movie

class RoleModelSerializerForPerson(serializers.ModelSerializer):
    movie = MovieModelSerializer()

    class Meta:
        model = Roles
        fields = (
            "role_type",
            "role_name",
            "movie",
        )
