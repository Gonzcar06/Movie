"""Persons URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import persons as person_views

router = DefaultRouter()
router.register(r'persons', person_views.PersonViewSet, basename='persons')

urlpatterns = [
    path('', include(router.urls))
]
