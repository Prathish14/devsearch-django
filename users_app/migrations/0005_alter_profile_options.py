# Generated by Django 4.2.5 on 2023-11-11 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created']},
        ),
    ]
