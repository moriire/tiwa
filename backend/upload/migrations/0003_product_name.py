# Generated by Django 4.2.6 on 2023-11-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='name', max_length=60),
            preserve_default=False,
        ),
    ]