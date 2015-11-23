# -*- coding: utf-8 -*-

from django.contrib import admin
from coffeecups.models import (
    Take, TakeForm, Throw, ThrowForm, Points, PointsForm, CupPolicy,
    CupPolicyForm)


class TakeAdmin(admin.ModelAdmin):
    model = TakeForm
    list_display = ('user', 'date',)
    search_fields = ('user__username',)


class ThrowAdmin(admin.ModelAdmin):
    model = ThrowForm
    list_display = ('user', 'date',)
    search_fields = ('user__username',)


class PointsAdmin(admin.ModelAdmin):
    model = PointsForm
    list_display = ('value',)
    search_fields = ('value',)


class CupPolicyAdmin(admin.ModelAdmin):
    model = CupPolicyForm
    list_display = ('name', 'comment', 'take_list', 'throw',)
    search_fields = ('name', 'comment', 'users__username',)

    def take_list(self, cup_policy):
        i = 0
        takes = '('
        for take in cup_policy.take.all():
            takes += '[{}: {}], '.format(i, take)
            i += 1
        takes += ')'

        return takes.strip()

admin.site.register(Take, TakeAdmin)
admin.site.register(Throw, ThrowAdmin)
admin.site.register(Points, PointsAdmin)
admin.site.register(CupPolicy, CupPolicyAdmin)
