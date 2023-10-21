# Generated by Django 5.0a1 on 2023-10-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(default='')),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]