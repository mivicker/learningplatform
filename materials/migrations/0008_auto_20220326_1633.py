# Generated by Django 3.2.12 on 2022-03-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0007_textbook_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="section",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="textbook",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
