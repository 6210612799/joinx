# Generated by Django 3.2.8 on 2021-10-29 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]