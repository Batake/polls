# Generated by Django 2.2 on 2019-05-05 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menus',
            new_name='votes',
        ),
    ]
