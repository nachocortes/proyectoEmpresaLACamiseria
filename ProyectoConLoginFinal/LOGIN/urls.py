from django.urls import path
from . import views

urlpatterns = [
    path('acocounts/', views.home_login, name="home_acocounts"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
