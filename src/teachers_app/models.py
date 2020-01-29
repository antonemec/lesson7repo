from django.db import models
from faker import Faker


# --------------------------------------------------------------------------------------------------------------
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    telephone = models.CharField(max_length=16)

    def get_info(self):
        return f'{self.first_name} {self.last_name}' \
               f'<br>Email: {self.email}' \
               f'<br>Phone: {self.telephone}'

    @classmethod
    def generate_teacher(cls):
        fake = Faker()

        a = f'{fake.phone_number}'

        teacher = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      email=fake.email(),
                      telephone=''.join(x for x in a if x.isdigit()))
        teacher.save()
        return teacher
# --------------------------------------------------------------------------------------------------------------
