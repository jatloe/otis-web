# Generated by Django 3.2.8 on 2021-10-17 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0058_alter_semesterdownloadfile_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemsuggestion',
            name='user',
            field=models.ForeignKey(help_text='User who suggested the problem.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
