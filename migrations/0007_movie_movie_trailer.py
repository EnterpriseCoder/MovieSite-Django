# Generated by Django 2.2.5 on 2019-10-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
