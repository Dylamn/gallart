from django.core.management.base import BaseCommand, CommandError
from gallart.gallery.models import Genre


class Command(BaseCommand):
    help = 'Create a new genre.'

    def add_arguments(self, parser):
        parser.add_argument('name', nargs='+', type=str)

    def handle(self, *args, **options):
        genre = Genre(name=options['name'])

        try:
            genre.save()
        except Exception:
            raise CommandError('The "%s" already exists.' % options['name'])

        self.stdout.write(
            self.style.SUCCESS('Sucessfully created the "%s" genre' % genre.name)
        )
