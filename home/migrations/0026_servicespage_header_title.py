# Generated by Django 4.2.5 on 2023-10-09 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_lawyer_is_first_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicespage',
            name='header_title',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Заголовок для поисковиков (если пустой, то по умолчанию название статьи)'),
        ),
    ]
