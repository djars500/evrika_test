import jwt
from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,PermissionsMixin
)
from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    leader = models.ForeignKey('self', on_delete=models.PROTECT, related_name='user_leader',null=True,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    objects = UserManager()

    def __str__(self):
        return self.email

