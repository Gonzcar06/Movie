"""Movies admin."""

# Django
from django.contrib import admin

# Model
from cride.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Circle admin."""

    list_display = (
        'title',
        'genre',
        'release_year',
        'casting',
    )

    
   
