# Generated by Django 3.2.3 on 2021-07-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20210728_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.SlugField(default=None, max_length=260, unique=True),
        ),
    ]