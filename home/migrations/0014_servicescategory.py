# Generated by Django 4.2.5 on 2023-09-29 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('home', '0013_contactinfo_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesCategory',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': 'Категории услуг',
            },
            bases=('wagtailcore.page',),
        ),
    ]