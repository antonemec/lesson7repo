from django.forms import ModelForm, Form, EmailField, CharField
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

from students_app.models import Student


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        with open('src/logs.txt', 'a') as text:
            text.write(f'\n---------------------------\n{datetime.now()} \nNew data in CONTACT: \nSubject: {subject}; \nMessage: {message}; '
                       f'\nEmail: {email_from} \n---------------------------\n')
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
