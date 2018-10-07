"""
beitech_store URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="invoice/orderlist.html")),
    path('admin/', admin.site.urls),
    path('docs/', include('rest_framework_docs.urls')),
    # API
    path('invoice/', include('invoice.urls',namespace='Invoice')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
