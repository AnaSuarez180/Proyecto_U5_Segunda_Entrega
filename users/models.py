from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group, Permission


from django.contrib.sessions.backends.db import SessionStore

# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=True)

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def get_by_natural_key(self, natural_key):
        return self.get(username=natural_key[0])

class AnonymousUser(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_authenticated = models.BooleanField(default=False)

class DifferentUsers():
    def create_user(self, email, username, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email= email, username=username, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_super_user(self, email, password, **extra_fields):
        extra_fields.setdefault('if_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario necesita que is_staff sea True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario necesita que is_superuser sea True')

        return self.create_user(email= email, password= password, **extra_fields)

    def create_anonymous_user():
        session = SessionStore()
        session.save()

        anonymous_user = AnonymousUser(session_key=session.session_key)
        anonymous_user.save()

