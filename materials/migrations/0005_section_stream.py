# Generated by Django 3.2.10 on 2022-01-16 22:06

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0004_section_time_to_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='stream',
            field=wagtail.core.fields.StreamField([('resource', wagtail.core.blocks.StructBlock([('resource', wagtail.images.blocks.ImageChooserBlock())])), ('headlineleftimage', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock())])), ('imagetopblock', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock())])), ('imagerightblock', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock())]))], default=''),
            preserve_default=False,
        ),
    ]
