from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import RegistroForm

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse

from email.mime.image import MIMEImage
import os


def registro(request):

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():

            # Crear el usuario
            form.save()

            # Autenticarlo para obtener el backend correcto
            usuario = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )

            if usuario is None:

                messages.error(
                    request,
                    "La cuenta fue creada, pero ocurrió un error al iniciar sesión."
                )

                return redirect("login")

            # Iniciar sesión
            login(request, usuario)

            # Intentar enviar el correo (si falla, no impedir el registro)

            try:

                html_message = render_to_string(
                    "usuarios/correo_bienvenida.html",
                    {
                        "usuario": usuario,
                        "catalogo_url": request.build_absolute_uri(reverse("catalogo")),
                    }
                )

                text_message = strip_tags(html_message)

                email = EmailMultiAlternatives(
                    subject="Bienvenido a la Biblioteca Comunitaria La Gomera",
                    body=text_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[usuario.email],
                )

                email.attach_alternative(html_message, "text/html")

                # Adjuntar el logo para usarlo como cid:logo
                logo_path = os.path.join(
                    settings.BASE_DIR,
                    "static",
                    "images",
                    "main-logo.png"
                )

                with open(logo_path, "rb") as f:

                    logo = MIMEImage(f.read())

                    logo.add_header("Content-ID", "<logo>")
                    logo.add_header(
                        "Content-Disposition",
                        "inline",
                        filename="main-logo.png"
                    )

                    email.attach(logo)

                email.send()

            except Exception as e:

                print(f"Error enviando correo: {e}")


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