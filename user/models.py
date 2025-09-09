from django.db import models
import uuid
from product.models import Product
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

class Country(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'country'
        managed = True
        verbose_name = 'country'
        verbose_name_plural = 'countries'

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    language = models.CharField(max_length=10, default='en')
    is_dark_mode = models.BooleanField(default=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='user_groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='user_permissions',
    )
    
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'username'
    objects = UserManager()

    class Meta:
        db_table = "user"
        unique_together = [('first_name', 'last_name')]
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    # CRITICAL: Add these methods for UUID compatibility
    def get_session_auth_hash(self):
        """Return the user's UUID as string for session authentication"""
        return str(self.id)
    
    def get_user_id(self):
        """Return user ID as string for session compatibility"""
        return str(self.id)

class Userinfo(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    address = models.TextField(blank=True, verbose_name="home address")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    birthdate = models.DateField(null=True)
    is_maried = models.BooleanField(default=False)
    
    class Meta:
        db_table = "user_info"
        verbose_name = 'user_info'
        verbose_name_plural = 'user_info'

class Review(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    review = models.TextField(blank=True)
    rating = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_positive = models.BooleanField(default=True)
    
    class Meta:
        db_table = "user_review"
        verbose_name = 'user_review'
        verbose_name_plural = 'user_reviews'