"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('cride.movies.urls', 'movies'), namespace='movies')),
    path('', include(('cride.persons.urls', 'persons'), namespace='persons')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls'))


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
