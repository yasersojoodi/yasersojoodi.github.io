# Generated by Django 4.0.1 on 2022-01-17 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_alter_message_c_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='person',
            name='conversations',
        ),
    ]