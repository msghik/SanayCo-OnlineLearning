# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(required = True, allow_null = False)
    last_name = serializers.CharField(required = True, allow_null = False)
    
    class Meta:
        model = CustomUser
        fields = ("__all__")
    

