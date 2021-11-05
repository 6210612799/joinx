# Generated by Django 3.2.8 on 2021-10-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_course_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='profile',
        ),
        migrations.AddField(
            model_name='user',
            name='degree',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.TextField(default='-', max_length=512),
        ),
    ]