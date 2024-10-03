from django.contrib import admin

# Register your models here.
from .models import Team, Teammate

admin.site.register(Team)
admin.site.register(Teammate)