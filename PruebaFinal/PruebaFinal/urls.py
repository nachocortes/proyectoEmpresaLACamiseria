from store.views import ProductoListView
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', ProductoListView.as_view(), name="index"),
    path('usuarios/login', views.login_view, name="login"),
    path('usuarios/logout', views.logout_view, name="logout"),
    path('usuarios/registro', views.register, name="register"),
    path('admin/', admin.site.urls),
    path('productos/', include('store.urls')),
    path('carrito/', include('carts.urls')),
    path('pedido/', include('pedidos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
