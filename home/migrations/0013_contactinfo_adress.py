# Generated by Django 4.2.5 on 2023-09-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_servicespage_subtitle_second_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='adress',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
    ]
