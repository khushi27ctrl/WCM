# Generated by Django 3.2.3 on 2021-06-16 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
    ]
