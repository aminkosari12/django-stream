from django.core.management import BaseCommand

from db.models import Admin

from faker import Faker


class Command(BaseCommand):
    help = "test one user in db"

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, help="number of loop")

    def handle(self, *args, **options):
        fake = Faker()
        user_lists = []
        for i in range(options['number']):
            user_lists.append(Admin.objects.create(username=fake.user_name(), email=fake.email(), password=fake.password()))
        print(user_lists)
