from django.db import models
from uuid import uuid4
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    """Manager for users."""
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a user."""
        if not email:
            raise ValueError("User must have an email.")
        
        if not password:
            raise ValueError("User must provide a password.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.is_user = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

    def create_taxi(self, email, password, **extra_fields):
        """Create and return a taxi driver account."""
        user = self.create_user(email, password)
        user.is_taxi = True

        user.save(using=self._db)

class User(AbstractBaseUser, PermissionsMixin):
    """Model of User"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(max_length=128, unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=17, blank=False)
    password = models.CharField(max_length=128, verbose_name="Password")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return f"{self.email}({self.id})"