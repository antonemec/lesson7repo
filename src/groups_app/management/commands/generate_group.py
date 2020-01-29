from django.core.management.base import BaseCommand
from groups_app.models import Group


class Command(BaseCommand):
    help = 'Generate 1 random group or num(if num set after command)'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        num = int(options.get('number') or 1)
        for _ in range(num):
            Group.generate_group()
