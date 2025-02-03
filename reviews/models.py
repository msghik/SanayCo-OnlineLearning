from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from courses.models import Course
from accounts.models import CustomUser

class Review(models.Model):
    
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} for {self.course.title} (rating: {self.rating})"
