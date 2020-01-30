import random

from django.core.management.base import BaseCommand
from students_app.models import Student
from groups_app.models import Group
from teachers_app.models import Teacher
from faker import Faker

fake = Faker()


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
        Teacher.objects.all().delete()

        a = f'{fake.phone_number}'

        teachers = [Teacher.objects.create(first_name=fake.first_name(),
                                           last_name=fake.last_name(),
                                           email=fake.email(),
                                           telephone=''.join(x for x in a if x.isdigit()))
                    for i in range(10)]

        groups = [Group.objects.create(name=f'{fake.first_name()} Group',
                                       description=f'{fake.text()}',
                                       curator=random.choice(teachers))
                  for i in range(10)]

        num = int(options.get('number') or 100)

        for _ in range(num):
            student = Student.generate_students()
            student.group = random.choice(groups)
            student.save()
