
# Generated by Django 3.2.3 on 2021-07-23 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210715_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('VI', 'video'), ('AU', 'audio'), ('IM', 'image'), ('SH', 'shared')], max_length=2),
        ),
    ]
