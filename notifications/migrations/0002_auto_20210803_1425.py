# Generated by Django 3.2.3 on 2021-08-03 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_room_room_id'),
        ('posts', '0004_alter_post_post_type'),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_comment', to='posts.comment'),
        ),
        migrations.AddField(
            model_name='notification',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_room', to='chat.room'),
        ),
    ]
