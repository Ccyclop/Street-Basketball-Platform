from django.contrib import admin

from .models import Team, Player, Feedback

class PlayerInline(admin.TabularInline):
    model = Player

class FeedbackInline(admin.TabularInline):
    model = Feedback

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [PlayerInline, FeedbackInline]