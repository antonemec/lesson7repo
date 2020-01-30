from django.db import models
from faker import Faker


# --------------------------------------------------------------------------------------------------------------
class Group(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=255,
                                   null=True, blank=True)
    curator = models.ForeignKey('teachers_app.Teacher',
                                null=True, blank=True,
                                on_delete=models.CASCADE)
    starosta = models.ForeignKey('students_app.Student',
                                 null=True, blank=True,
                                 on_delete=models.CASCADE,
                                 related_name="+",)

    def get_info(self):
        r = self.description.split('.')
        return f"{self.name}({self.id}) " \
               f"<br>_________________________<br>" \
               f"Description: \n{'<br>'.join(r)}"

    @classmethod
    def generate_group(cls):
        fake = Faker()

        group = cls(name=f'{fake.first_name()} Group',
                    description=f'{fake.text()}')
        group.save()
        return group
