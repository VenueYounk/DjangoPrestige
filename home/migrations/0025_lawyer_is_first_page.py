# Generated by Django 4.2.5 on 2023-10-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_remove_lawyer_education_lawyer_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='is_first_page',
            field=models.BooleanField(default=False, verbose_name='Выводить на главную страницу'),
        ),
    ]
