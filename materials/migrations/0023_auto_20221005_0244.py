# Generated by Django 3.2.12 on 2022-10-05 02:44

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0022_rename_notes_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tip',
            old_name='tip_body',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='section',
            name='slides',
            field=wagtail.core.fields.StreamField([('resource', wagtail.core.blocks.StructBlock([('resource', wagtail.images.blocks.ImageChooserBlock())])), ('baseblock', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock())])), ('questionblock', wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.TextBlock()), ('choice_1', wagtail.core.blocks.TextBlock()), ('choice_2', wagtail.core.blocks.TextBlock()), ('choice_3', wagtail.core.blocks.TextBlock()), ('choice_4', wagtail.core.blocks.TextBlock()), ('correct', wagtail.core.blocks.ChoiceBlock(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]))])), ('headlineleftimage', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('imagetopblock', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('imagerightblock', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))]),
        ),
    ]
