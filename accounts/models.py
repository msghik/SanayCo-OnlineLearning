from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom user manager to create users and superusers with a phone number.
    """
    def create_user(self, phone_number, email, password=None, **extra_fields):
        print('create_user')
        if not phone_number:
            raise ValueError("The Phone Number field is required.")
        if not email:
            raise ValueError("The Email field is required.")
        
        email = self.normalize_email(email) if email else None
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email= None, password=None, **extra_fields):
        print('create_superuser')
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, email, password, **extra_fields)


class CustomUser(AbstractUser):
    
    full_name = models.CharField(max_length=255, blank = True)
    phone_number = models.CharField(max_length=15, unique=True)
    username = None

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'phone_number'
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.phone_number
