from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('register_user/' , views.UserViewSet.as_view({'post': 'create'})),
]
