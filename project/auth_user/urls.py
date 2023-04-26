from django.urls import path
from . import views

urlpatterns = [
    path('createUser', views.create_user, name='newuser'),
    path('login', views.login_, name='login'),
    path('logout', views.logout_, name='logout'),
]