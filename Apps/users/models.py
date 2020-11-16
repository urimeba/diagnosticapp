from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
    generos  = [
            ('H', 'Hombre'),
            ('M', 'Mujer')
        ]

    class Meta:
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

    genero = models.CharField(max_length=1, choices=generos, blank=False, null=True, verbose_name = 'Genero')
    edad = models.PositiveIntegerField()
