from rest_framework import serializers
from .models import CustomUser
import re

class UserSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(required=True, allow_null=False)
    last_name = serializers.CharField(required=True, allow_null=False)
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.CharField(read_only=True)
    # phone_number = serializers.CharField(required = True, allow_null = False)
    
    class Meta:
        model = CustomUser
        fields = ("__all__")

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Za-z]", value):
            raise serializers.ValidationError("Password must contain at least one letter.")
        if not re.search(r"\d", value):
            raise serializers.ValidationError("Password must contain at least one number.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):    
            raise serializers.ValidationError("Password must contain at least one special character.")
        
        return value

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) != 11:
            raise serializers.ValidationError("Phone number must be exactly 11 digits long.")
        
        return value
        
    
    # def create(self, validated_data):
        
        
    #     groups = validated_data.pop('groups', [])
    #     user_permissions = validated_data.pop('user_permissions', [])
    #     password = validated_data.pop('password')

    #     # user = CustomUser(**validated_d)
    #     user = CustomUser.objects.create(**validated_data)
        
    #     user.set_password(password)  
    #     user.save()

    #     user.groups.set(groups)
    #     user.user_permissions.set(user_permissions)
    #     # CustomUser.objects


    #     return user
    

