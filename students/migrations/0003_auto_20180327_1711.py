# Generated by Django 2.0.3 on 2018-03-27 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20180327_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='surname',
        ),
    ]
