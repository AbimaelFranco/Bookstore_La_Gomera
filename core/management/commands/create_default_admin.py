from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = "Create default superuser if it doesn't exist"

    def handle(self, *args, **options):
        username = os.environ["ADMIN_USERNAME"]

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.SUCCESS("Superuser already exists.")
            )
            return

        User.objects.create_superuser(
            username=username,
            email=os.environ["ADMIN_EMAIL"],
            password=os.environ["ADMIN_PASSWORD"],
        )

        self.stdout.write(
            self.style.SUCCESS("Superuser created successfully.")
        )