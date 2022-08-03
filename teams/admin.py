from django.contrib import admin

from .models import Team, Player

class PlayerInline(admin.TabularInline):
    model = Player

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline]