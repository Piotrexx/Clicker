from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator
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

class User(AbstractBaseUser):
    name = models.CharField(max_length=250, unique=True)
    score = models.IntegerField(default=0)
    ship_upgrade = models.IntegerField(default=1, validators =[MinValueValidator(1)])
    money = models.IntegerField(default=0)
    objects = CustomUserManager()

    USERNAME_FIELD = 'name'

class Planet(models.Model):
    name = models.CharField(max_length=250)
    distance = models.IntegerField()
