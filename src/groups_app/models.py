from django.db import models
from faker import Faker


# --------------------------------------------------------------------------------------------------------------
class Group(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255,
                                   null=True, blank=True)

    def get_info(self):
        r = self.description.split('.')
        return f"{self.name}({self.id}) " \
               f"<br>_________________________<br>" \
               f"Description: \n{'<br>'.join(r)}"

    @classmethod
    def generate_group(cls):
        fake = Faker()

        group = cls(name=f'{fake.first_name()} INC',
                    description=f'{fake.text()}')
        group.save()
        return group
