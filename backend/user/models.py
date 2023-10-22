from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext as _
from django.utils import timezone
from .manager import CustomUserManager
from rest_framework import serializers
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_("email address"), unique=True,)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name",  "last_name"]

    def __str__(self):
        return self.email


    def absolute_url(self):
        return reverse('flash-detail', args=(self.id,))

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
 
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from allauth.account import app_settings as allauth_account_settings
    
class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

class UserDetailsSerializer(UserDetailsSerializer):
    class Meta:   
        model = User
        fields = ["pk", "email"]