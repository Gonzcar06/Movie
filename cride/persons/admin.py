"""Persons admin."""

# Django
from django.contrib import admin

# Model
from cride.persons.models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    """Circle admin."""

    list_display = (
        'first_name',
        'last_name',
        'aliases',

    )

    
   