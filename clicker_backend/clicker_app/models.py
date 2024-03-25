from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create(self, **kwargs):
        return self.create_user(**kwargs)
    
    def create_user(self, name,password, **kwargs):
        if not name:
            return ValueError('The name is required ')

        user = self.model(name=name **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_verified', True)
        return self.create_user(name=name, password=password, **extra_fields)

class Ship(AbstractBaseUser):
    name = models.CharField(max_length=250)
    score = models.IntegerField(default=0)


class Planet(models.Model):
    name = models.CharField(max_length=250)
    distance = models.IntegerField()
