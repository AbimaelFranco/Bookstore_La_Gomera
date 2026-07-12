from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from django.conf import settings

from .forms import RegistroForm


def registro(request):

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():

            usuario = form.save()

            # Iniciar sesión automáticamente
            login(request, usuario)

            # Enviar correo de bienvenida
            send_mail(
                subject="Bienvenido a la Biblioteca Comunitaria La Gomera",

                message=f"""
Hola {usuario.first_name},

Tu cuenta ha sido creada correctamente en la Biblioteca Comunitaria La Gomera.

Tu nombre de usuario es:
{usuario.username}

Ya puedes iniciar sesión y explorar nuestro catálogo.

¡Gracias por formar parte de nuestra comunidad!
""",

                from_email=settings.DEFAULT_FROM_EMAIL,

                recipient_list=[
                    usuario.email
                ],

                fail_silently=False,
            )

            messages.success(
                request,
                "Tu cuenta fue creada correctamente."
            )

            return redirect("catalogo")

    else:

        form = RegistroForm()


    return render(
        request,
        "usuarios/registro.html",
        {
            "form": form
        }
    )