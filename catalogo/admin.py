from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Libro

admin.site.register(Categoria)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):

    list_display = (
        "miniatura",
        "codigo",
        "titulo",
        "autor",
        "categoria",
        "cantidad_disponible",
        "estado_fisico",
    )

    list_display_links = ("titulo",)

    search_fields = (
        "codigo",
        "titulo",
        "autor",
    )

    list_filter = (
        "categoria",
        "estado_fisico",
    )

    ordering = ("codigo",)

    def miniatura(self, obj):
        if obj.portada:
            return format_html(
                '<img src="{}" width="50" style="border-radius:4px;">',
                obj.portada.url
            )
        return "—"

    miniatura.short_description = "Portada"