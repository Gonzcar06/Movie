"""Movies admin."""

# Django
from django.contrib import admin

# Model
from cride.movies.models import Movie
from cride.movies.models import Roles
from cride.movies.models import Genre

class Rolesss(admin.TabularInline):
    model = Roles
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Circle admin."""
    inlines = [Rolesss]
    list_display = (
        'title',
        'genre_t',
        'release_year',
        #'inlines'
    )
    extra = 1
#admin.site.register(Movie, PersonAdmin)
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
