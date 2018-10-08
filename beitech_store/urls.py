"""
beitech_store URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', TemplateView.as_view(template_name="invoice/orderlist.html")),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Invoice API', public=False)),
    # API
    path('invoice/', include('invoice.urls', namespace='invoice')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
