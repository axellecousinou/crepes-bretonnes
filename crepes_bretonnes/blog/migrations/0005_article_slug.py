# Generated by Django 2.1.15 on 2021-05-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210506_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
