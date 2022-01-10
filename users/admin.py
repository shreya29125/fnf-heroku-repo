from django.contrib import admin
from users.models import Profile, FollowRequest

# Register your models here.
admin.site.register(Profile)
admin.site.register(FollowRequest)