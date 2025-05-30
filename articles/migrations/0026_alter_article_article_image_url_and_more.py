# Generated by Django 5.1.4 on 2025-05-08 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_alter_article_created_at_alter_review_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image_url',
            field=models.ImageField(blank=True, null=True, upload_to='article_images/local/'),
        ),
        migrations.AlterField(
            model_name='articlepdf',
            name='pdf_file_url',
            field=models.FileField(blank=True, null=True, upload_to='article_pdfs/local/'),
        ),
    ]
