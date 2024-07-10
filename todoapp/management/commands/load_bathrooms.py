from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Clears existing data and loads bathrooms fixtures'

    def handle(self, *args, **options):
        self.stdout.write('Flushing database...')
        call_command('flush', '--noinput')

        self.stdout.write('Loading bathrooms fixtures...')
        call_command('loaddata', 'bathrooms.yaml')

        self.stdout.write(self.style.SUCCESS('Successfully loaded bathrooms fixtures.'))
