from django.db import models

import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .managers import CustomUserManager

class Test(models.Model):
    test_char = models.CharField(max_length = 50)
    test_int = models.IntegerField()

    def __str__(self):
        return self.test_char

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    STUDENT = 2
    TEACHER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STUDENT, 'STUDENT'),
        (TEACHER, 'TEACHER')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    # Roles created here
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    # created_date = models.DateTimeField(default=timezone.now)
    # modified_date = models.DateTimeField(default=timezone.now)
    # created_by = models.EmailField(blank = True)
    # modified_by = models.EmailField(blank = True)
    password = models.CharField(max_length=128)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class user_otp(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    otp = models.IntegerField()

    def __str__(self):
        return self.user
