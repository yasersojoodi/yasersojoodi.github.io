# Generated by Django 4.0.1 on 2022-01-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_message_c_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='c_id',
            field=models.CharField(max_length=1, null=True),
        ),
    ]