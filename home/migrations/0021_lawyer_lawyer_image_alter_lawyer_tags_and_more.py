# Generated by Django 4.2.5 on 2023-10-08 18:18

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('home', '0020_alter_lawyerservicescategoryrelationship_lawyer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='lawyer_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='lawyer',
            name='tags',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='home.servicescategory'),
        ),
        migrations.AlterField(
            model_name='lawyerservicescategoryrelationship',
            name='lawyer',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lawyer', to='home.lawyer'),
        ),
        migrations.AlterField(
            model_name='lawyerservicescategoryrelationship',
            name='services_category',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_category', to='home.servicescategory'),
        ),
    ]