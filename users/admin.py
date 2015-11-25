# -*- coding: utf-8 -*-

from django.contrib import admin
from users.models import Profile, ProfileForm


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ('user', 'rfid_tag', 'favorite_song',)
    search_fields = ('user__username', 'rfid_tag', 'favorite_song',)

admin.site.register(Profile, ProfileAdmin)
