# Generated by Django 2.2.6 on 2020-12-25 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Url',
            new_name='UrlAddress',
        ),
    ]
