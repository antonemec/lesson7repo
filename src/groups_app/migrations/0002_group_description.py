# Generated by Django 2.2.9 on 2020-01-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]