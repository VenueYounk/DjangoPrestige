# Generated by Django 4.2.5 on 2023-09-23 05:24

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('text', wagtail.blocks.RichTextBlock(features=['h2', 'bold', 'italic'], help_text='Основной контент', label='Текст')), ('image', wagtail.blocks.StructBlock([('caption', wagtail.blocks.CharBlock()), ('img', wagtail.images.blocks.ImageChooserBlock())], label='Картинка с подписью')), ('quotes', wagtail.blocks.RichTextBlock()), ('list', wagtail.blocks.RichTextBlock())], default={}, use_json_field=True),
        ),
    ]
