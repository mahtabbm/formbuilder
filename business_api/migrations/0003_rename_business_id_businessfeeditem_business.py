# Generated by Django 3.2.5 on 2021-07-29 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_api', '0002_businessfeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessfeeditem',
            old_name='business_id',
            new_name='business',
        ),
    ]
