# Generated by Django 3.2.12 on 2022-03-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0011_resourceaccess_access_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='resource_type',
            field=models.CharField(default='I', max_length=1),
        ),
    ]