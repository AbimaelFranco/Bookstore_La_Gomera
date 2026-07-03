from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Libro, Categoria


def catalogo(request):

    categorias_principales = Categoria.objects.filter(
        principal=True
    ).order_by("nombre")

    categoria_id = request.GET.get("categoria")

    libros = Libro.objects.select_related(
        "categoria"
    ).order_by("titulo")

    categoria_actual = None

    if categoria_id:
        categoria_actual = get_object_or_404(
            Categoria,
            id=categoria_id
        )

        libros = libros.filter(
            categoria=categoria_actual
        )

    paginator = Paginator(libros, 4)  # 4 x 5

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "catalogo/catalogo.html",
        {
            "categorias": categorias_principales,
            "categoria_actual": categoria_actual,
            "page_obj": page_obj,
        },
    )

def detalle_libro(request, codigo):

    libro = get_object_or_404(
        Libro,
        codigo=codigo
    )

    return render(
        request,
        "catalogo/detalle_libro.html",
        {
            "libro": libro
        }
    )