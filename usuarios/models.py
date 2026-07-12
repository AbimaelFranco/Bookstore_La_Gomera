from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):

    class Sexo(models.TextChoices):
        MASCULINO = "M", "Masculino"
        FEMENINO = "F", "Femenino"
        OTRO = "O", "Prefiero no decir"

    class NivelEducativo(models.TextChoices):
        PRIMARIA = "PRI", "Primaria"
        BASICOS = "BAS", "Básicos"
        DIVERSIFICADO = "DIV", "Diversificado"
        UNIVERSIDAD = "UNI", "Universidad"
        POSTGRADO = "POS", "Postgrado"

    email = models.EmailField(
        unique=True,
        verbose_name="Correo electrónico"
    )

    fecha_nacimiento = models.DateField(
        blank=True
    )

    comunidad = models.CharField(
        max_length=150,
        blank=True
    )

    nivel_educativo = models.CharField(
        max_length=3,
        choices=NivelEducativo.choices,
        blank=True
    )

    sexo = models.CharField(
        max_length=1,
        choices=Sexo.choices
    )

    def __str__(self):
        return self.username