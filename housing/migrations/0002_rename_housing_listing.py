# Generated by Django 3.2.7 on 2021-11-11 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Housing',
            new_name='Listing',
        ),
    ]
