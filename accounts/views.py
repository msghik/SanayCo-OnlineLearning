from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import viewsets, status

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
