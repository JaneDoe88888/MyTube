# Generated by Django 4.2.2 on 2023-07-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0004_video_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
