# Generated by Django 4.0.4 on 2022-04-27 00:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rus', '0006_rename_image_yengliklarru_imagee'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('info', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
