"""Circles URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import movies as movie_views

router = DefaultRouter()
router.register(r'movies', movie_views.MoviesViewSet, basename='movies')

urlpatterns = [
    path('', include(router.urls))
]
