# -*- coding: utf-8 -*-

from django.contrib import admin
from checkpoints.models import Point, PointForm, Check, CheckForm


class PointAdmin(admin.ModelAdmin):
    form = PointForm
    list_display = ('id', 'name', 'comment', 'arduino', 'bonus',)
    search_fields = ('name', 'comment', 'arduino', 'bonus',)


class CheckAdmin(admin.ModelAdmin):
    form = CheckForm
    list_display = ('id', 'user', 'point', 'date',)
    search_fields = ('user__username', 'point__name', 'date',)

admin.site.register(Point, PointAdmin)
admin.site.register(Check, CheckAdmin)
