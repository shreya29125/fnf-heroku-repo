# Generated by Django 3.2.3 on 2021-07-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210723_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_id',
            field=models.CharField(max_length=60, primary_key=True, serialize=False, unique=True),
        ),
    ]
