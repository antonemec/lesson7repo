from django.core.management.base import BaseCommand
from teachers.models import Teacher


class Command(BaseCommand):
    help = 'Generate 1 random teacher or num(if num set after command)'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        num = int(options.get('number') or 1)
        for _ in range(num):
            Teacher.generate_teacher()