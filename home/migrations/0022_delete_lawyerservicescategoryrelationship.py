# Generated by Django 4.2.5 on 2023-10-08 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_lawyer_lawyer_image_alter_lawyer_tags_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LawyerServicesCategoryRelationship',
        ),
    ]
