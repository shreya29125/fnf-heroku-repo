# Generated by Django 3.2.3 on 2021-07-28 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20210726_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='is_archived',
        ),
        migrations.RemoveField(
            model_name='story',
            name='is_expired',
        ),
    ]