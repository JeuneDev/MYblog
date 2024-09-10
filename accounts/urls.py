from django.urls import path
from .views import register, CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'auth'

urlpatterns = [
    path('register/', register, name='register'),  # Page d'inscription
    path('login/', CustomLoginView.as_view(), name='login'),  # Page de connexion
    path('logout/', LogoutView.as_view(), name='logout'),  # Page de déconnexion
]
