# Generated by Django 3.2.12 on 2022-03-28 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0012_resource_resource_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resource",
            name="resource_type",
            field=models.CharField(
                choices=[
                    ("video", "video"),
                    ("image", "image"),
                    ("pdf", "pdf"),
                    ("gloss", "glossary"),
                ],
                default="image",
                max_length=5,
            ),
        ),
    ]
