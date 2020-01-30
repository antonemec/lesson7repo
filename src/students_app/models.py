from django.db import models
from faker import Faker


# --------------------------------------------------------------------------------------------------------------
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True,
                                  default=None)
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=16)
    address = models.CharField(max_length=255,
                               null=True, blank=True)
    group = models.ForeignKey('groups_app.Group',
                              null=True, blank=True,
                              on_delete=models.CASCADE)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'

    def get_all_info(self):
        return f'{self.first_name} {self.last_name} (ID: {self.id})' \
               f'<br>Birth date: {self.birth_date}' \
               f'<br>Email: {self.email}' \
               f'<br>Phone: {self.telephone}'

    def get_id(self):
        return f'{self.id}'

    @classmethod
    def generate_students(cls):
        fake = Faker()

        a = f'{fake.phone_number}'

        student = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      birth_date=fake.date_of_birth(tzinfo=None, minimum_age=10, maximum_age=60),
                      email=fake.email(),
                      telephone=''.join(x for x in a if x.isdigit()),
                      address=fake.address())
        student.save()
        return student
