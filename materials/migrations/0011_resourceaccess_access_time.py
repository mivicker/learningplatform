# Generated by Django 3.2.12 on 2022-03-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0010_resourceaccess"),
    ]

    operations = [
        migrations.AddField(
            model_name="resourceaccess",
            name="access_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
