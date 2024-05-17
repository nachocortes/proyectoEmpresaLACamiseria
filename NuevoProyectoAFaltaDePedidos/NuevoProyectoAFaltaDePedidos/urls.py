from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('LOGIN.urls')),
    path('', include('STORE.urls')),
    path('ventas/', include('VENTAS.urls')),
# path('rrhh/', include('VENTAS.urls')),
# path('crm/', include('VENTAS.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)