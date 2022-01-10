# Generated by Django 3.2.3 on 2021-07-23 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0005_alter_room_room_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=16)),
                ('team_description', models.CharField(max_length=400)),
                ('room', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='chat.room')),
                ('team_members', models.ManyToManyField(related_name='teams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamAddRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests_sent', to='teams.team')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_requests_recieved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
