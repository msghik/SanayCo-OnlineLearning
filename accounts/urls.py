from django.contrib import admin
from django.urls import path, include
from . import views
from .views import UserSearchView


urlpatterns = [
    path('register_user/' , views.UserViewSet.as_view({'post': 'create'})),
    
    path('search/', UserSearchView.as_view(), name='user-search'),
]
