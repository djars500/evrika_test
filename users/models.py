import jwt
from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,PermissionsMixin
)
from django.contrib.auth.models import (
	BaseUserManager,
)


class UserManager(BaseUserManager):
    
    def create_user(self, email,username,is_staff, password=None):
        
        if username is None:
            raise TypeError('Users must have a username.')
        
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username,email=self.normalize_email(email), is_staff=is_staff)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email,username,is_staff, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email,username,is_staff,password )
        user.is_superuser = True
        
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    leader = models.ForeignKey('self', on_delete=models.PROTECT, related_name='user_leader',null=True,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','is_staff']


    objects = UserManager()

    def __str__(self):
        return self.email

