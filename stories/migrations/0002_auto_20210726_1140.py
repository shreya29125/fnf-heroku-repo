# Generated by Django 3.2.3 on 2021-07-26 06:10

from django.db import migrations, models
import stories.utils


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='expired',
            new_name='is_expired',
        ),
        migrations.AddField(
            model_name='story',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='story',
            name='story_type',
            field=models.CharField(choices=[('VI', 'video'), ('AU', 'audio'), ('IM', 'image'), ('SH', 'shared')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='story',
            name='content',
            field=models.FileField(blank=True, upload_to=stories.utils.upload_path_handler),
        ),
    ]
