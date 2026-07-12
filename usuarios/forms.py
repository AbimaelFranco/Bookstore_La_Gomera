from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import Usuario


class RegistroForm(UserCreationForm):

    email = forms.EmailField(
        label="Correo electrónico",
        required=True
    )

    class Meta:
        model = Usuario

        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "fecha_nacimiento",
            "comunidad",
            "nivel_educativo",
            "sexo",
            "password1",
            "password2",
        )

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombres"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Apellidos"
            }),

            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre de usuario"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Correo electrónico"
            }),

            "fecha_nacimiento": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "comunidad": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Comunidad"
            }),

            "nivel_educativo": forms.Select(attrs={
                "class": "form-select"
            }),

            "sexo": forms.Select(attrs={
                "class": "form-select"
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Contraseña"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Confirmar contraseña"
        })

        self.fields["first_name"].label = "Nombres"
        self.fields["last_name"].label = "Apellidos"
        self.fields["username"].label = "Nombre de usuario"

    def clean_email(self):

        email = self.cleaned_data["email"].lower()

        if Usuario.objects.filter(email=email).exists():
            raise ValidationError(
                "Ya existe una cuenta registrada con este correo."
            )

        return email

    def clean_username(self):

        username = self.cleaned_data["username"]

        if Usuario.objects.filter(username__iexact=username).exists():
            raise ValidationError(
                "Ese nombre de usuario ya está en uso."
            )

        return username

    def save(self, commit=True):

        usuario = super().save(commit=False)

        usuario.email = self.cleaned_data["email"].lower()

        if commit:
            usuario.save()

        return usuario