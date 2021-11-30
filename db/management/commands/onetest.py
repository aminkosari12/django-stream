from django.core.management import BaseCommand
from db.models import Admin

from faker import Faker


class Command(BaseCommand):
    help = "test one user in db"

    def handle(self, *args, **options):
        fake = Faker()
        s = Admin.objects.create(username=fake.user_name(), email=fake.email(), password=fake.password())
        print(s)
