import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **options):
        username = os.environ.get("ADMIN_USERNAME")
        password = os.environ.get("ADMIN_PASSWORD")
        try:
            admin = User.objects.create_superuser(username=username, password=password)
            admin.save()
            print("Test-Admin account created")
        except:
            print("Admin user alredy has been created")