# Generated by Django 4.2.2 on 2023-07-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0003_alter_video_dislikes_alter_video_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(null=True),
        ),
    ]
