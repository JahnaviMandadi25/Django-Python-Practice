from django.conf import settings  # For accessing settings like DEBUG and MEDIA_URL
from django.conf.urls.static import static  # For serving media files in development
from django.contrib import admin
from django.urls import path, include  # For URL path handling

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Include application URLs (your main app's URLs)
    path('', include('myapp.urls')),
]

# Serve media files during development (only when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
