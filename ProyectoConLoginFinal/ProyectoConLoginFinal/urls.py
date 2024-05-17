from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('LOGIN.urls')),
    path('store/', include('STORE.urls')),
]