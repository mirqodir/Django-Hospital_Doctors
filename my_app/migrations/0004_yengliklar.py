# Generated by Django 4.0.4 on 2022-04-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yengliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yanglik', models.TextField()),
                ('ism', models.TextField()),
                ('vaqt', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
