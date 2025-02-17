from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Category
        fields = ('__all__')
        read_only_fields = ['created_at', 'updated_at']
        
        def validate_name(self, value):
            if len(value) < 3:
                raise serializers.ValidationError("Category name must be at least 3 characters long.")
            return value
