# Generated by Django 2.2.5 on 2019-10-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20191022_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(default='', upload_to='movies_banner'),
            preserve_default=False,
        ),
    ]
