"""
beitech_store URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('invoice/', include('invoice.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
