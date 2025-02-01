from django.db import models
from django.conf import settings

class Course(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'instructor'},  # optional filter
        related_name='courses_instructed'
    )
    
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='courses_enrolled', 
        blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
