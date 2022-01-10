# Generated by Django 3.2.3 on 2021-07-15 13:12

from django.db import migrations, models
import django.db.models.deletion
import posts.utils


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210703_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='parent_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shared_posts', to='posts.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, upload_to=posts.utils.upload_path_handler),
        ),
    ]