# Generated by Django 2.2.5 on 2020-03-20 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_superhost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avarta',
            new_name='avatar',
        ),
    ]
