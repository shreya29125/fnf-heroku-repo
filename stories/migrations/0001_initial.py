# Generated by Django 3.2.3 on 2021-07-25 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(blank=True, upload_to=posts.utils.upload_path_handler)),
                ('expired', models.BooleanField(default=False)),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]