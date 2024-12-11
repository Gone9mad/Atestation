from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    ROLES = (('buyer', 'buyer'), ('salesman', 'salesman'), ('haven t decided yet', 'haven t decided yet'))

    username = None

    first_name = models.CharField(max_length=50, verbose_name='Name', **NULLABLE)
    last_name = models.CharField(max_length=70, verbose_name='Family', **NULLABLE)
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email', help_text='Email')
    avatar = models.ImageField(verbose_name='Avatar', help_text='Avatar', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    role = models.CharField(max_length=100, choices=ROLES, verbose_name='Role')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.emai

    class Meta:
        verbose_name='User'
        verbose_name_plural = 'Users'
