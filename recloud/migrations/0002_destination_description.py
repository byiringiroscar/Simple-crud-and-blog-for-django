# Generated by Django 3.2.6 on 2021-08-26 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='description',
            field=models.TextField(default=0, max_length=2000),
            preserve_default=False,
        ),
    ]