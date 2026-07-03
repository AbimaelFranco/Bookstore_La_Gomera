from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("<int:codigo>/", views.detalle_libro, name="detalle_libro"),
]