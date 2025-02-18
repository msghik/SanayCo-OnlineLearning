from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
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

from rest_framework import generics
from rest_framework.response import Response
from .documents import CustomUserDocument
from .models import CustomUser
from .serializers import UserSerializer 

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        Search the 'accounts_index' using ?q=<term>.
        We'll do a simple match on the 'username' field as an example.
        """
        query = self.request.query_params.get('q', None)
        if query:
            search = CustomUserDocument.search().query("match", username=query)
            results = search.execute()


            user_ids = [hit.meta.id for hit in results]

            return CustomUser.objects.filter(pk__in=user_ids)

        return CustomUser.objects.all()
