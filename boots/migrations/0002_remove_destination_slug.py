# Generated by Django 3.1.4 on 2021-09-07 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='slug',
        ),
    ]