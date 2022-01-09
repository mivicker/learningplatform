# Generated by Django 3.2.10 on 2022-01-07 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_section_time_to_complete'),
        ('users', '0005_enrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='history',
            field=models.ManyToManyField(blank=True, related_name='course_history', to='materials.Textbook'),
        ),
    ]