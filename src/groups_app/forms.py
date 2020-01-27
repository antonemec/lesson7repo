from django.forms import ModelForm, Form, EmailField, CharField
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

from groups_app.models import Group


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data

        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        with open('logs.txt', 'a') as text:
            text.write(f'{datetime.now()} - New data in CONTACT_STUDENTS: Subject: {subject}; Message: {message}; '
                       f'Email from: {email_from} \n')


class GroupsAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
