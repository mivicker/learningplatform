# Generated by Django 3.2.10 on 2022-01-07 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_auto_20211224_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='time_to_complete',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
