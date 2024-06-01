from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Загрузка всех фикстур'

    def handle(self, *args, **options):
        management.call_command('loaddata', 'app_profile/fixtures/users.json')
        management.call_command('loaddata', 'app_profile/fixtures/profiles.json')
        management.call_command('loaddata', 'app_profile/fixtures/profile_avatars.json')
        management.call_command('loaddata', 'app_market/fixtures/genres.json')
        management.call_command('loaddata', 'app_market/fixtures/tags.json')
        management.call_command('loaddata', 'app_market/fixtures/cycles.json')
        management.call_command('loaddata', 'app_market/fixtures/books.json')
        management.call_command('loaddata', 'app_market/fixtures/book_images.json')
