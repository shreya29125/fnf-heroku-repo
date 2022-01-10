# Generated by Django 3.2.3 on 2021-11-26 16:21

from django.db import migrations, models
import posts.utils


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_remove_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='default.png', upload_to=posts.utils.upload_path_handler),
        ),
    ]
