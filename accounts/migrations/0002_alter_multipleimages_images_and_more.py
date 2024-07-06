# Generated by Django 5.0.6 on 2024-07-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimages',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='multiple_images/'),
        ),
        migrations.AlterField(
            model_name='shortreels',
            name='short_reel',
            field=models.FileField(blank=True, null=True, upload_to='shortreels/'),
        ),
    ]
