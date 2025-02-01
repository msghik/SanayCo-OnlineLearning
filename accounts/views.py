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
    
    # def create(self, request, *args, **kwargs):
    #     user_serializer = serializers.UserSerializer(data=request.data)
    #     user_serializer.is_valid(raise_exception=True)

    #     # Use the custom user manager to create the user
    #     user_obj = models.CustomUser.objects.create(
    #         username=user_serializer.validated_data['username'],
    #         email=user_serializer.validated_data['email'],
    #         phone_number=user_serializer.validated_data['phone_number'],
    #         password=user_serializer.validated_data['password']
    #     )
        
    #     return Response({"detail": "User successfully created"}, status=status.HTTP_201_CREATED)

    
