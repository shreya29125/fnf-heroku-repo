# Generated by Django 3.2.3 on 2021-12-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_alter_story_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='story_type',
            field=models.CharField(choices=[('VI', 'video'), ('AU', 'audio'), ('IM', 'image')], default=None, max_length=2),
        ),
    ]
