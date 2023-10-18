# Generated by Django 4.2.5 on 2023-09-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Основной номер телефона')),
                ('second_phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Дополнительный номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('vk_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на VK')),
                ('telegram_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на Telegram')),
                ('whatsapp_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на WhatsApp')),
            ],
            options={
                'verbose_name': 'Контактная информация',
                'verbose_name_plural': 'Контактная информация',
            },
        ),
    ]
