# Generated by Django 5.1.4 on 2025-05-08 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0014_alter_communityarticle_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='banner_pic_url',
            field=models.FileField(null=True, upload_to='community_images/local/'),
        ),
        migrations.AlterField(
            model_name='community',
            name='profile_pic_url',
            field=models.FileField(null=True, upload_to='community_images/local/'),
        ),
    ]
