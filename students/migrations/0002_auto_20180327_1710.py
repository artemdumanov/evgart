# Generated by Django 2.0.3 on 2018-03-27 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='surname',
            new_name='last_name',
        ),
    ]
