# Generated by Django 4.2.6 on 2023-11-09 19:21

from django.db import migrations, models
import django.db.models.deletion
import upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pic',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='desc',
        ),
        migrations.AddField(
            model_name='upload',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_upload', to='upload.product'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='img',
            field=models.ImageField(upload_to=upload.models.upload_location),
        ),
    ]
