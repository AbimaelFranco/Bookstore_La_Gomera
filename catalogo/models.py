from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100,
        unique=True
    )
    Descripcion = models.TextField(
        max_length=500,
        blank=True
    )

    principal = models.BooleanField(
        default = False
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
    
class EstadoFisico(models.TextChoices):
    EXCELENTE = "Excelente", "Excelente"
    BUENO = "Bueno", "Bueno"
    REGULAR = "Regular", "Regular"
    MALO = "Malo", "Malo"

class Libro(models.Model):

    # Añadir: Paginas, donador, idioma, fecha publicacion

    codigo = models.BigAutoField(
    primary_key=True,
    verbose_name="Código"
    )

    isbn = models.CharField(
    max_length=20,
    unique=True,
    blank=True,
    null=True,
    verbose_name="ISBN",
    default=None
    )

    titulo = models.CharField(
        max_length=200
    )

    autor = models.CharField(
        max_length=150
    )

    editorial = models.CharField(
        max_length=20,
        default=""
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="libros"
    )

    cantidad_disponible = models.PositiveIntegerField(
        default=1
    )

    estado_fisico = models.CharField(
        max_length=20,
        choices=EstadoFisico.choices,
        default=EstadoFisico.BUENO
    )

    resumen = models.TextField(
        max_length=500,
        blank=True
    )

    comentarios = models.TextField(
        max_length=200,
        blank=True
    )

    portada = models.ImageField(
    upload_to="portadas/",
    blank=True,
    null=True,
    verbose_name="Portada"
    )

    class Meta:
        ordering = ["codigo"]
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return f"{self.codigo} - {self.titulo}"