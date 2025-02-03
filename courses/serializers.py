from rest_framework import serializers
from .models import Course
from categories.serializers import CategorySerializer
from categories.models import Category

class CourseSerializer(serializers.ModelSerializer):
    
    users = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ('__all__')

    def get_users(self, obj):
        
        return [f"{user.first_name} {user.last_name}" for user in obj.users.all()]
    
    
    
