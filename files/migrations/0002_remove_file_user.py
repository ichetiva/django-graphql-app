# Generated by Django 3.2.19 on 2023-06-27 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='user',
        ),
    ]