from django.contrib import admin
from teams.models import Team, TeamAddRequest

# Register your models here.
admin.site.register(Team)
admin.site.register(TeamAddRequest)