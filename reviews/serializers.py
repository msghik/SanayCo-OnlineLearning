from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    
    user_information = serializers.SerializerMethodField()
    course_information = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = ('__all__')

    def get_user_information(self,obj):
        
        user = obj.user
        
        return {
            "username": user.username,
            "full_name": f"{user.first_name} {user.last_name}",
            "email": user.email,
        }
        
    def get_course_information(self, obj):
        
        course = obj.course
        
        return {
            "id": course.id,
            "title": course.title,
        }
        
