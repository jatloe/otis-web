# Generated by Django 3.2.6 on 2021-08-15 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0066_alter_studentregistration_graduation_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='num_units_done',
        ),
    ]