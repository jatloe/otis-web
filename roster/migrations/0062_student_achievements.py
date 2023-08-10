# Generated by Django 3.2.5 on 2021-08-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        # ("dashboard", "0029_auto_20210804_1857"),
        ("roster", "0061_alter_registrationcontainer_allowed_tracks"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="achievements",
            field=models.ManyToManyField(
                help_text="Codes that this student has obtained",
                to="dashboard.AchievementCode",
            ),
        ),
    ]
