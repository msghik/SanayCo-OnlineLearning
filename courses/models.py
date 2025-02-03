from django.db import models
from accounts.models import CustomUser
from categories.models import Category

class Course(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    instructor = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'instructor'}, 
        related_name='courses_instructed'
    )
    
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    users = models.ManyToManyField(
        CustomUser, 
        related_name='courses_enrolled', 
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=False)
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE, 
        related_name='courses', 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return self.title
