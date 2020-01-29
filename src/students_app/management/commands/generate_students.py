import random

from django.core.management.base import BaseCommand
from students_app.models import Student, Group


class Command(BaseCommand):
    help = 'Generate 100 random students'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        Group.objects.all().delete()
        Student.objects.all().delete()

        groups = [Group.objects.create(name=f'name_{i}')
                  for i in range(10)]

        num = int(options.get('number') or 100)

        for _ in range(num):
            student = Student.generate_students()
            student.group = random.choice(groups)
            student.save()
