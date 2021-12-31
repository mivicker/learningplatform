# Generated by Django 3.2.6 on 2021-12-07 16:24

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("materials", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="grade",
            old_name="user",
            new_name="student",
        ),
        migrations.AlterUniqueTogether(
            name="grade",
            unique_together={("student", "section")},
        ),
    ]
