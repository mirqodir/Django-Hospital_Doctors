# Generated by Django 4.0.4 on 2022-04-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postru',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='postru',
            name='staji',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='postru',
            name='talim',
            field=models.TextField(),
        ),
    ]
